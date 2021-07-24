from elasticsearch import Elasticsearch, helpers
import requests
import sys, json

import requests
res = requests.get('http://localhost:9200')
print(res.content)

es=Elasticsearch()

#def load_json(file):
 #   yield json.load(file)
    
file='harvard_dataverse.json'
    
with open(file, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())
    

#helpers.bulk(es, load_json(json_input), index='my-index', doc_type='my-type')
es.index(index="my_index", doc_type='doc', body='data')