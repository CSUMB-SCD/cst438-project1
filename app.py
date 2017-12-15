from flask import Flask, render_template, jsonify, request, session, url_for, redirect, flash
from urllib2 import Request, urlopen, URLError
from flask_pymongo import PyMongo
# import requests
import os
from flask_cors import CORS
import json
import bcrypt

app = Flask(__name__)
# sess = Session()
# string user = os.environ['user']
# pwd = os.environ['dbpwd']

app.config['MONGO_DBNAME'] = 'recipe_finder_users'
# app.config['MONGO_URI'] = 'mongodb://'+os.environ['user']+':'+os.environ['dbpwd'] +'@ds155325.mlab.com:55325/recipe_finder_users'
app.config['MONGO_URI'] = 'mongodb://'+'utsab'+':'+'testing'+'@ds155325.mlab.com:55325/recipe_finder_users'
mongo = PyMongo(app)

# app.secret_key = 'secretkey'
app.config['SECRET_KEY'] = 'secretkey'
# sess.init_app(app)
CORS(app)
# app.config['SECRET_KEY'] = 'secretkey'
# app.config['SESSION_TYPE'] = 'mongodb'
# session.permanent = True


@app.route('/nutrition')
def nutrition():
    return render_template('guestNutrition.html')
app.route('')
@app.route('/guestNutrition')
def nutrition1():
    return render_template('guestNutrition.html',name=os.environ['appId'],key=os.environ['appKey'])
@app.route('/login', methods=['POST', 'GET'])
def login2():
    error = None
    if request.method == 'POST':
        users = mongo.db.users
        # hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        hashpass = request.form['pass']
        user = users.find_one({'username' : request.form['name']})
        if user is None:

             error = 'Invalid username or password. Please try again!'

        else:
            if user['password'] == hashpass:
                print 'user exists!'
                session['username'] = request.form['name']
                print user['password']
                return redirect(url_for('home'))
            else:
                error = 'Invalid username or password. Please try again!'

        return render_template('login.html',error=error)
        #return redirect(url_for(,error=error)

        # if users.find( { $and: [ { username : request.form['username']}, {password : request.form['password'] } ] }  ):
        #     return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        users = mongo.db.users
        user = users.find_one({'username' : request.form['regname']})
        print 'After find_one is called'
        if user is None:
            # todo: check if password == confirm password
            if request.form['regpass'] != request.form['reregpass']:
                error = "Passwords do not match"
                return render_template('login.html',error=error)
            # hashpass = bcrypt.hashpw(request.form['regpass'].encode('utf-8'), bcrypt.gensalt())
            hashpass = request.form['regpass']
            users.insert({'username' : request.form['regname'], 'password' : hashpass, 'recipe' : 'null'})
            session['username'] = request.form['regname']
            return redirect(url_for('home'))
        error="Sorry Username is taken!"
        return render_template('login.html',error=error)


    if request.method == 'GET':
        return ''
@app.route('/home')
def home():
    print 'inside home function!'
    if 'username' in session:
        print 'inside session'
        # app.secret_key = session['username']
        # return 'You are logged in as ' +  session['username']
        print 'inside ' + session['username'] + 's profile!'
        return render_template('userHome.html')
    return 'ERROR: PREVIOUS USER HAS BEEN LOGGED OUT'
@app.route('/userNutrition')
def userNutrition():
    return render_template('userNutrition.html',name=os.environ['appId'],key=os.environ['appKey'])
    # return redirect(url_f)
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
@app.route('/home',methods=['GET'])
def addRecipe():
    print "addRECIPE function!"
    print '!!!!!!!! IN ADD FUNCTION !!!!!!'
    print request.form['submit']
    users = mongo.db.users
    user = users.find_one({'username' : session['username']})
    print session['username']
    if user is None:
        print 'User doesnt exist!'
        return 'ERROR: PREVIOUS USER HAS BEEN LOGGED OUT'
    else:
        print 'User exists!'
        # for doc in user['recipe']
        #     print(doc)
        print user['recipe']  #null
        print user
        if user['recipe'] == 'null':
            user['recipe'] = request.form['submit']
        #else:
        # print users
        # users.update_one({user['_id']},{ "$set": { "recipe": request.form['submit']} })
        # users.update({user['_id']},{ "$set": { "recipe": request.form['submit']} })
        print user['recipe']
        users.save(user)
        return Response(user['recipe'])
@app.route('/recipe')
def recipe():
    users = mongo.db.users
    user = users.find_one({'username' : session['username']})
    userRecipe = user['recipe']
    return render_template('userRecipe.html', recipe = userRecipe)

        # users.update_one(
        # {"username": session['username']},
        # {
        # "$set": {
        #     "link" :
        # }
        # }
    # )
        # return redirect(url_for('login2'))
        # return redirect(url_for('results')) # do something
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
@app.route('/logout')
def logout():
    app.secret_key = 'no user'
    session.pop('username', None)
    return redirect(url_for('login'))
@app.route('/chat')
def chat():
    return render_template('chat2.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8080), debug=True)
    # app.run(
    # host=os.getenv('IP', '0.0.0.0'),
    # port=int(os.getenv('PORT', 8080)),
    # debug=True
    # )
