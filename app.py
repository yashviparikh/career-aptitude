from flask import Flask,render_template,request,jsonify
from careers import CAREERS,RELATED_KEYWORDS,recommend_careers
app= Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        selected_keywords=request.form.getlist("keywords")
        careers=recommend_careers(selected_keywords)
        return render_template("results.html",careers=careers)
    return render_template("index.html",keywords=list(CAREERS.keys()))

@app.route("/related_keywords",methods=["POST"])
def get_related_keywords():
    selected=request.json.get("selected_keywords",[])
    suggestions=set()

    for keyword in selected:
        if keyword in RELATED_KEYWORDS:
            suggestions.update(RELATED_KEYWORDS[keyword])
            print("suggestions:",list(suggestions))
    return jsonify(list(suggestions))
if __name__=="__main__":
    app.run(debug=True)