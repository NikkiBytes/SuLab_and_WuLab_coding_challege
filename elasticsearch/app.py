from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
import json

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():

    # field list for selection menu
    fields=['@context', '@id', '@type', 'author', 'citation', 'creator', 'dateModified', 'datePublished', 'description', 'distribution', 'funder', 'identifier', 'includedInDataCatalog', 'keywords', 'license', 'name', 'provider', 'publisher', 'spatialCoverage', 'temporalCoverage', 'version', 'author.@id', 'author.affiliation', 'author.identifier', 'author.name', 'citation.@id', 'citation.@type', 'citation.identifier', 'citation.text', 'creator.@id', 'creator.affiliation', 'creator.identifier', 'creator.name', 'distribution.@id', 'distribution.@type', 'distribution.contentSize', 'distribution.contentUrl', 'distribution.description', 'distribution.fileFormat', 'distribution.identifier', 'distribution.name', 'funder.@type', 'funder.name', 'includedInDataCatalog.@type', 'includedInDataCatalog.name', 'includedInDataCatalog.url', 'license.@type', 'license.text', 'license.url', 'provider.@type', 'provider.name', 'publisher.@type', 'publisher.name']

    # input values
    queryID=request.args.get("queryID")
    queryField=request.args.get("queryField")
    queryKeyword=request.args.get("queryKeyword")
    queryBonus=request.args.get("queryBonus")

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

        try:
            # search ES index with ID query
            res=es.search(index="harvardmetadata", doc_type="metadata", body=query_id)
             # pull the number of hits found
            hits=res['hits']['total']['value']

            # format object data
            if hits == 1:
                template="single_hit.html"
                hit_obj = res['hits']['hits'][0]["_source"]
                data_json=json.dumps(hit_obj, separators=(',', ':'), indent=4)

            return render_template(template, fields=fields, response=data_json, queryID=queryID)

        except:
            return render_template("single_hit.html", fields=fields, response="ERROR")


    elif queryKeyword is not None:

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

        try:
            # search ES index with keyword field query
            res=es.search(index="harvardmetadata", doc_type="metadata", body=query_field)
            # pull the number of hits found
            hits=res['hits']['total']['value']
            # format object data
            if hits == 1:
                template="single_hit.html"
                hit_obj = res['hits']['hits'][0]["_source"]
                data_json=json.dumps(hit_obj, separators=(',', ':'), indent=4)
                return_data=data_json

            elif hits > 1:
                template="multi_hits.html"
                hits_list=res["hits"]["hits"]
                data_list=[]
                for obj in hits_list:
                    data_json=json.dumps(obj["_source"], separators=(',', ':'), indent=4)
                    data_list.append(data_json)
                return_data=data_list

            return render_template(template, fields=fields, response=return_data, queryField=queryField, queryKeyword=queryKeyword)

        except:
            return render_template("single_hit.html", fields=fields, response="ERROR")

    elif queryBonus is not None:
        facet_query={
          "size":0,
          "aggs": {
            "facets": {
              "terms": {
                "field": "funder.name.keyword"
                    }
                }
              }
            }
        res=es.search(index="harvardmetadata", doc_type="metadata", body=facet_query)
        facet_buckets=res["aggregations"]["facets"]['buckets']
        facet_dict={}
        for bucket in facet_buckets:
            key=bucket['key']
            doc_ct=bucket['doc_count']
            print(key,doc_ct)
            facet_dict[key]=doc_ct
        data_json=json.dumps(facet_dict, separators=(',', ':'), indent=4)
        return render_template("facet.html", fields=fields, facet_dict=facet_dict, json=data_json)


    return render_template("index.html", fields=fields)




if __name__=="__main__":
    app.run(debug=True, port=8000)
