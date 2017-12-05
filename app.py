from flask import Flask, render_template,jsonify,request
from urllib2 import Request, urlopen, URLError
# import requests
import os
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/guestNutrition')
def nutrition():
    return render_template('guestNutrition.html',name=os.environ['appId'],key=os.environ['appKey'])
@app.route('/login')
def login2():
    return render_template('login.html')
@app.route('/')
def login():
  return render_template('login.html')
@app.route('/guest')
def guest():
    return render_template('guestHome.html')
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
@app.route('/nutritionApi/v1_1/search/<phrase>',methods=['GET'])
def nutritionApi(phrase):
    print phrase
    request=Request('https://api.nutritionix.com/v1_1/search/'+phrase+'?appId='+os.environ['appId']+'&appKey='+os.environ['appKey'])
    try:
        key=os.environ['appKey']
        applicationId=os.environ['appId']
        response=urlopen(request)
        nutrition=response.read()
        jsonObject=json.loads(nutrition)
        print jsonObject['hits']
        return jsonify({'hits':jsonObject})
    except URLError, e:
        print ' Got an error code:', e
@app.route('/guestHome')
def guestHome():
	return render_template('guestHome.html') 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8080), debug=True)
    # app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    # debug=True
    # )
