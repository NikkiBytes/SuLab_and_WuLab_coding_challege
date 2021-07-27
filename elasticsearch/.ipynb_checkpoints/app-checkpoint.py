from flask import Flask, render_template, request  
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    
    q = request.form.get("q")
    if q is not None:
        return render_template("index.html")
    
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)