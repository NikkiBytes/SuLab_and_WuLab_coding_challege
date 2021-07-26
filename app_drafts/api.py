"""
Su Lab and Wu Lab Coding Challenge API 2021
Author: Nichollette Acosta

Main points:
The API should allow users to query by two methods.
1. users should be able to query by a specific dataset identifier as indicated by the '@id' field in the data file (e.g., "https://doi.org/10.11588/data/0HJAJS"). 

2. users should be able to query by a specific field in the JSON object (e.g., datasets with "Earth and Environmental Sciences" in the keywords). 

The output of this web API by either query method should be the matching metadata object(s) in JSON format.

"""


# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
  


  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)