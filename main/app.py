from flask import Flask, render_template,jsonify
import request
from flask_cors import CORS
import json
 
app = Flask(__name__)
CORS(app)
search_url="http://www.recipepuppy.com/about/api/"
@app.route('/')
def home():
  return render_template('home.html')
  # have to use the server to make an api call here currently not working
@app.route('',methods=['POST'])
def results():
    jsonObj = request.json
    dataDict = json.dumps(jsonObj)
    data = json.loads(dataDict) 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)