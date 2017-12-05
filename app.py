from flask import Flask, render_template, jsonify, request, session, url_for, redirect
from urllib2 import Request, urlopen, URLError
from flask_pymongo import PyMongo
# import requests
import os
from flask_cors import CORS
import json
import bcrypt

app = Flask(__name__)
CORS(app)
# string user = os.environ['user']
# pwd = os.environ['dbpwd'] 
userKey = ''
app.config['MONGO_DBNAME'] = 'recipe_finder_users'
# app.config['MONGO_URI'] = 'mongodb://'+os.environ['user']+':'+os.environ['dbpwd'] +'@ds155325.mlab.com:55325/recipe_finder_users'
app.config['MONGO_URI'] = 'mongodb://'+'nhipolito'+':'+'project1' +'@ds155325.mlab.com:55325/recipe_finder_users'
mongo = PyMongo(app)
@app.route('/nutrition')
def nutrition():
    return render_template('guestNutrition.html')
@app.route('/login', methods=['POST', 'GET'])
def login2():
    return ''
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        user = users.find_one({'username' : request.form['username']})
        if user is None:
            # todo: check if password == confirm password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('home'))
            # return render_template('userHome.html')
        return 'User already exists!';
    if request.method == 'GET':
        return ''
@app.route('/home')
def home():
    if 'username' in session:
        app.secret_key = session['username']
        print app.secret_key
        # return 'You are logged in as ' +  session['username']
        return render_template('userHome.html')
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
    app.secret_key = 'secretkey'
    app.run(host='0.0.0.0', port=int(8080), debug=True)
    # app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    # debug=True
    # )
