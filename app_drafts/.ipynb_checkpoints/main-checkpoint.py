"""
Su Lab and Wu Lab Coding Challenge API 2021
Author: Nichollette Acosta

Main points:
The API should allow users to query by two methods.
1. users should be able to query by a specific dataset identifier as indicated by the '@id' field in the data file (e.g., "https://doi.org/10.11588/data/0HJAJS"). 

2. users should be able to query by a specific field in the JSON object (e.g., datasets with "Earth and Environmental Sciences" in the keywords). 

The output of this web API by either query method should be the matching metadata object(s) in JSON format.

"""


from flask import Flask
from api.elastic_test import connect_elasticsearch
from api.insert_data import *
from api.retrieve_data import *


app = Flask(__name__)


if __name__ = '__main__':
    app.run()