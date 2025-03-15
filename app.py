from flask import Flask,render_template,request,jsonify
import json
app= Flask(__name__)

CAREERS={
    "analytical":["Data Scientist","Statistician""Financial Analyst"],
    "creative": ["Graphic Designer", "Copywriter", "Marketing Specialist"],
    "technical": ["Software Developer", "Cybersecurity Expert", "AI Engineer"],
    "social": ["HR Manager", "Teacher", "Counselor"]
}

def recommended_careers(keywords):
    recommended=[]
    for keyword in keywords:
        if keyword in CAREERS:
            recommended.extend(CAREERS[keyword])
    return list(set(recommended))[:10]
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        selected_keywords=request.form.getlist("keywords")
        careers=recommended_careers(selected_keywords)
        return render_template("results.html",careers=careers)
    return render_template("index.html",keywords=CAREERS.keys())
if __name__==("__main__"):
    app.run(debug=True)