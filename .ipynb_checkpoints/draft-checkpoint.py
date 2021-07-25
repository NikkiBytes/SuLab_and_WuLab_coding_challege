from elasticsearch import Elasticsearch, helpers
#import requests
from datetime import datetime
import sys, json
# Connection String

#print(res.content)

#es=Elasticsearch()
#es = Elasticsearch([{'host': 'elasticsearch.dev.anaconda.com', 'port': 9200}])
es = Elasticsearch( )#['host'], scheme="http", port=9200)

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
print(res['result'])

#def load_json(file):
 #   yield json.load(file)

file='harvard_dataverse.json'

with open(file, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())


#helpers.bulk(es, load_json(json_input), index='my-index', doc_type='my-type')
#es.index(index="my_index", doc_type='doc', body='data')
