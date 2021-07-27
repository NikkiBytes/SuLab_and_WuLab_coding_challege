from flask import Flask, render_template, request  
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    
    q=request.args.get("q")
    #q = request.form.get("q")
    if q is not None:
        
        res=es.search(index="harvardmetadata", body={"query": {"match_all":{}}})
        return render_template("index.html", q=q, response=res )

    return render_template("index.html", q=q)




if __name__=="__main__":
    app.run(debug=True, port=8000)