from flask import Flask, render_template,jsonify,request
from urllib2 import Request, urlopen, URLError
# import requests
import os
from flask_cors import CORS
import json
 
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
  return render_template('home.html')
  # have to use the server to make an api call here include url in the post method
@app.route('/todo/api/v0.1/results/<results_id>',methods=['GET'])
def results(results_id):
    print results_id
    request = Request('http://www.recipepuppy.com/api/?i=' + results_id)
    try:
	    response = urlopen(request)
	    receipe = response.read()
	    jsonObject = json.loads(receipe)
	    print jsonObject['results']
	    return jsonify({'results': jsonObject})
    except URLError, e:
        print ' Got an error code:', e
    
    # jsonObj = request.json
    # dataDict = json.dumps(jsonObj)
    # data = json.loads(dataDict) 
    # console.log(data)
@app.route('/login')
def login():
	return render_template('login.html') 

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=int(8080), debug=True)
    app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    )