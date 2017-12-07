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

app.config['MONGO_DBNAME'] = 'recipe_finder_users'
# app.config['MONGO_URI'] = 'mongodb://'+os.environ['user']+':'+os.environ['dbpwd'] +'@ds155325.mlab.com:55325/recipe_finder_users'
app.config['MONGO_URI'] = 'mongodb://'+'utsab'+':'+'testing'+'@ds155325.mlab.com:55325/recipe_finder_users'
mongo = PyMongo(app)

@app.route('/nutrition')
def nutrition():
    return render_template('guestNutrition.html')
@app.route('/guestNutrition')
def nutrition1():
    return render_template('guestNutrition.html',name=os.environ['appId'],key=os.environ['appKey'])
@app.route('/login', methods=['POST', 'GET'])
def login2():
    if request.method == 'POST':
        users = mongo.db.users
        hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        user = users.find({'username' : request.form['username'], 'password' : hashpass})
        if user is None:
            print 'user doesnt exist!'
            return 'User doesnt exist'
        else:
            print 'user exists!'
            session['username'] = request.form['username']
            return redirect(url_for('home'))

        # if users.find( { $and: [ { username : request.form['username']}, {password : request.form['password'] } ] }  ):
        #     return redirect(url_for('home'))
    if request.method == 'GET':
        return ''
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        print 'Inside register'
        user = users.find_one({'username' : request.form['username']})
        print 'After find_one is called'
        if user is None:
            # todo: check if password == confirm password
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            print session['username']
            print 'Registering user!'
            return redirect(url_for('home'))
        print user
        print request.form['username']
        return 'User already exists!';
    if request.method == 'GET':
        return ''
@app.route('/home')
def home():
    if 'username' in session:
        app.secret_key = session['username']
        # return 'You are logged in as ' +  session['username']
        print 'inside ' + session['username'] + 's profile!'
        return render_template('userHome.html')
    return 'user doesnt exist but still tried to proceed to home?'
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
@app.route('/addRecipe',methods=['POST'])
def addRecipe():
    if request.method == 'POST':
        print request.form['submit']
        pass # do something
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
        # print jsonObject['hits']
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
