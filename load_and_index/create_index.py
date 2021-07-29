from elasticsearch import Elasticsearch
import json, os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Elastic search configuation
es = Elasticsearch(HOST="http://localhost", PORT=9200)


file='harvard_dataverse.json'

with open(file, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())

for obj in data:
    #print("-----")
    obj_id=obj["@id"]
    es.index(index="harvardmetadata", doc_type="metadata", id=obj_id, body=obj,request_timeout=10000)

es.indices.put_mapping(
    index="harvardmetadata",
    doc_type="metadata",
    include_type_name=True,
    body=
    {
        'properties': {
            '@context': {
                'type': 'text',
                'fields': {
                    'keyword': {
                        'type': 'keyword', 'ignore_above': 256}}},
    '@id': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    '@type': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    'author': {'properties': {'affiliation': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'citation': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'text': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'creator': {'properties': {'affiliation': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'dateModified': {'type': 'date'},
    'datePublished': {'type': 'date'},
    'description': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    'distribution': {'properties': {'@id': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      '@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'contentSize': {'type': 'long'},
      'fileFormat': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'identifier': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'funder': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'identifier': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    'includedInDataCatalog': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'url': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'keywords': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    'license': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'text': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'name': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
    'provider': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'publisher': {'properties': {'@type': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
      'name': {'type': 'text',
       'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}},
    'version': {'type': 'text',
     'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}}

)


print("[INFO] completed loading and indexing ES.")
