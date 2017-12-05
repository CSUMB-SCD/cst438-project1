from flask import Flask, render_template,jsonify,request,url_for,session,redirect
from urllib2 import Request, urlopen, URLError
from flask_pymongo import PyMongo
from flask_mongo_sessions import MongoDBSessionInterface
# import requests
import os
from flask_cors import CORS
import json
#TODO Put import into a inport file if time permits for clean up

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recipe-finder'
app.config['MONGO_URI'] = 'mongodb://Discharg:SEproject@ds125716.mlab.com:25716/recipe-finder'
mongo = PyMongo(app)
with app.app_context():
    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')


CORS(app)
@app.route('/nutrition')
def nutrition():
    print mongo.db.users.find_one({'username' : 'carlos'})
    return render_template('guestNutrition.html')
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
