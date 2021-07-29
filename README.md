# Simple Elasticsearch API  

## Instructions  
This assumes you have the Elasticsearch server installed and the Python Flask and Elasticsearch packages installed.

### Installation:  
> [Elasticsearch server](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)     
  
> Install Flask [docs](https://flask.palletsprojects.com/en/2.0.x/installation/)  

`> pip install Flask`  
  
  
> Install Elasticsearch Python Package [docs](https://elasticsearch-py.readthedocs.io/en/v7.13.4/)  

`> pip install elasticsearch`



### Setup and Run App  
  
1. Start elasticsearch server  
In your terminal change directory to where you have downloaded the elasticsearch server and start the server.  
`> cd C:\elasticsearch-7.13.4\elasticsearch-7.13.4`  
`> .\bin\elasticsearch.bat`   
  
2. Load and index the data into Elasticsearch  
Run the script to automatically load and index the harvard metadata dateset into ES.   
Script is `create_index.py` is located in the `load_and_index/` folder. 
`> python create_index.py` or `python load_and_index/create_index.py` 

3. Run local flask app   
`python app.py` or `python elasticsearch/app.py`







Notes/Assumptions:
* for the output I removed the elasticsearch tags, such as the "_shards", "hits", etc. fields.
* currently using the "match_phrase" for the query for keywords, therefore results with exact phrases and word proximity provided 
