from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    
    # field list for selection menu
    fields=['@context', '@id', '@type', 'author', 'citation', 'creator', 'dateModified', 'datePublished', 'description', 'distribution', 'funder', 'identifier', 'includedInDataCatalog', 'keywords', 'license', 'name', 'provider', 'publisher', 'spatialCoverage', 'temporalCoverage', 'version']
    
    # input values
    queryID=request.args.get("queryID")
    queryField=request.args.get("queryField")
    queryKeyword=request.args.get("queryKeyword")
    #q = request.form.get("q")
    
    if queryID is not None:
   
        # Elasticsearch query for an id
        query_id={
            "query": {
                "ids" : {
                    "type" : "metadata",
                    "values" : [queryID]
                        }
                     }
            }

        res=es.search(index="harvardmetadata", doc_type="metadata", body=query_id)
        
        return render_template("index.html", fields=fields, response=res)
    
    if queryKeyword is not None:
        
        # Elasticsearch Query for a specific field 
        query_field={
          "query": {
              "match_phrase": {
                queryField: {
                  "query": queryKeyword
                }
            }
          }
        }
        
        # search ES index
        res=es.search(index="harvardmetadata", doc_type="metadata", body=query_field)
        # pull the number of hits found
        hits=res['hits']['total']['value']
        # format object data
        if hits == 1:
            hit_obj = res['hits']['hits'][0]
            data_json=json.dumps(hit_obj, separators=(',', ':'), indent=4)
        return render_template("index.html", fields=fields, response=data_json)
    
    return render_template("index.html", x=queryID, y=queryField, z=queryKeyword, fields=fields)




if __name__=="__main__":
    app.run(debug=True, port=8000)
    

