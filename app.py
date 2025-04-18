from flask import Flask,render_template,request,jsonify
from careers import tech_skill_preferences_data,recommend_tech_careers
app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/keywords", methods=["GET","POST"])
def index():
    if request.method=="POST":
        selected_skills=request.form.getlist("skills")
        if not selected_skills:
            return render_template("index.html",skills=get_all_skills(),error="no skill selected")
        preferences=request.form.getlist("preferences")
        careers=recommend_tech_careers(selected_skills,include_scores=False,filter_preferences=preferences)
        return render_template("results.html",careers=careers)
    return render_template("index.html",skills=get_all_skills())

def get_all_skills():
    skills=set()
    for category,details in tech_skill_preferences_data.items():
        skills.update(details["skills"])
    return sorted(list(skills))

@app.route("/related_keywords",methods=["POST"])
def get_related_keywords():
    selected=list(set(request.json.get("selected_skills",[])))
    if not selected:
        return jsonify({"error": "no skills selected"}),400
    suggestions=set()
    visited=set(selected)
    maxdepth=3

    def fetch_related(keys,depth=0):
        if depth>=maxdepth:
            return
        new_skills=set()
        for key in keys:
            for category,details in tech_skill_preferences_data.items():
                if key in details["skills"]:
                    for domain,domain_details in details["domains"].items():
                        for role in domain_details["roles"]:
                            related_skills=details["skills"]
                            for skill in related_skills:
                                if skill not in visited:
                                    visited.add(skill)
                                    suggestions.add(skill)
                                    new_skills.add(skill)
        if new_skills:
            fetch_related(new_skills,depth+1)
    fetch_related(selected)
    return jsonify(sorted(list(suggestions)))
if __name__=="__main__":
    app.run(debug=True)