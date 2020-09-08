from elasticsearch import Elasticsearch, exceptions
import os
import time
from flask import Flask, jsonify, request, render_template
import sys
import requests
import simplejson as json

#es = Elasticsearch(host='es')
es = Elasticsearch(host='http://ec2-54-214-200-23.us-west-2.compute.amazonaws.com')
uri = 'http://ec2-54-214-200-23.us-west-2.compute.amazonaws.com:9200/codata/_search'

app = Flask(__name__)


###########
### APP ###
###########
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    key = request.args.get('q')
    if not key:
        return jsonify({
            "status": "failure",
            "msg": "Please provide a query"
        })

    query = json.dumps({

           "query" : {"multi_match" : {
               "query" : key,
               "fields" : ["STATE", "CITY", "ADDRESS", "ZIP", "SITE", "COUNTY"],
                "type":     "most_fields"
           }}
    })
    response = requests.get(uri,   headers={"Content-type":"application/json"}, data=query)
    results = json.loads(response.text)

    sites_list = [{"site":  v['_source']['SITE_'],
               "address":  v['_source']['ADDRESS'],
               "city":  v['_source']['CITY'],
               "state":  v['_source']['STATE'],
               "latitude":  v['_source']['LATITUDE'],
               "longitude":  v['_source']['LONGITUDE']
               }  for v in results['hits']['hits']]
    #x = json.dumps({"sites": sites_list,
    #           "hits" : len(sites_list)})
    hits = len(sites_list)

    return jsonify({
        "sites": sites_list,
        "hits": hits,
        "status": "success"
    })

if __name__ == "__main__":

  uri_search = 'http://ec2-54-214-200-23.us-west-2.compute.amazonaws.com:9200/codata/_search'
  #ENVIRONMENT_DEBUG = os.environ.get("DEBUG", False)
  #check_and_load_index()
  #testsearch(uri_search)
  app.run(host='0.0.0.0', port=5000)
