from flask import Flask, render_template, request, jsonify
from careers import tech_skill_preferences_data, recommend_tech_careers
from roadmap import addurl

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/keywords", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_skills = request.form.getlist("skills")
        if not selected_skills:
            return render_template("index.html", skills=get_all_skills(), error="no skill selected")
        preferences = request.form.getlist("preferences")
        careers = recommend_tech_careers(selected_skills, include_scores=False, filter_preferences=preferences)
        careers_with_url = addurl(careers)
        return render_template("results.html", careers=careers_with_url)
    return render_template("index.html", skills=get_all_skills())

def get_all_skills():
    skills = set()
    for category, details in tech_skill_preferences_data.items():
        skills.update(details["skills"])
    return sorted(list(skills))

@app.route("/related_keywords", methods=["POST"])
def get_related_keywords():
    selected = list(set(request.json.get("selected_skills", [])))
    if not selected:
        return jsonify({"error": "no skills selected"}), 400
    
    # Create a map of skills to their categories
    skill_categories = {}
    for category, details in tech_skill_preferences_data.items():
        for skill in details["skills"]:
            if skill not in skill_categories:
                skill_categories[skill] = set()
            skill_categories[skill].add(category)
    
    # for every selected skill,add its category to selected_categories
    selected_categories = set()
    for skill in selected:
        if skill in skill_categories:
            selected_categories.update(skill_categories[skill])
    
    # Get all skills from selected categories
    suggestions = set()
    for category in selected_categories:
        if category in tech_skill_preferences_data:
            suggestions.update(tech_skill_preferences_data[category]["skills"])
    
    # Remove already selected skills
    suggestions = suggestions - set(selected)
    
    return jsonify(sorted(list(suggestions)))

if __name__ == "__main__":
    app.run(debug=True)
