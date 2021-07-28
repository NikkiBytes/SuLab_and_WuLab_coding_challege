from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    
    q=request.args.get("q")
    #q = request.form.get("q")
    if q is not None:
        
        query={
            "query": {
                "ids" : {
                    "type" : "metadata",
                    "values" : [q]
                        }
                     }
            }

        
        res=es.search(index="harvardmetadata", doc_type="metadata", body=query)
        

        return render_template("index.html", q=q, response=res)

    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True, port=8000)
    
#def format_data(data, data_list):

#dict_hits=(res["hits"]["hits"])
#data_list=[]
#for x in dict_hits:
 #   data=x["_source"]["message"]
    #format_data(data, data_list)
  #  data_list.append(data)
#json_str=json.dumps(dict_hits, separators=(',', ':'), indent=4)
#json_str=json_str.replace("\n", "")