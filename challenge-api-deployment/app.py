"""
Importing libraries to create flask app
for house price prediction

"""
import flask
from flask import json, request
import pickle
import numpy as np
import pandas as pd
from flask import jsonify
import os
from validate.validation import validate
from pydantic import ValidationError

"""
Initializing app and loading model pickle file

"""

app = flask.Flask(__name__)
app.config["DEBUG"] = True
pipe = pickle.load(open('model/pipe.pkl','rb'))

"""
Creating homepage with GET method to check if the api is alive

"""

@app.route('/',methods= ['GET'])
def home():
    return 'Alive'

"""
Providing user information what information is
required to receive price prediction using GET method

"""

@app.route('/predict',methods=['GET'])
def info():
    return """
    "data": {
    "proprety_type": str
    "bedrooms": int 
    "area": int
    "equipped_kitchen": Optional[str] 
    "furnished": Optional[bool] 
    "open_fire": Optional[bool] 
    "terrace": Optional[bool]
    "terrace_area": Optional[int] 
    "garden": Optional[bool] 
    "garden_area": Optional[int] 
    "surface" = Optional [int] 
    "surface_plot": Optional[int] 
    "facade": Optional[int] 
    "state": Optional[Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]]
    "swimming_pool": Optional[bool] 
    "Address": Optional[str]
     }
    """


"""
Taking user input from post method, validating the information and
predicting the price

"""

@app.route('/predict',methods=['POST'])   
def post_info():
    user_input = request.get_json(force=True)
    try:
        input_validation = validate(**user_input)
    except ValidationError as e:
        return e.json()
    data_df = pd.DataFrame(user_input, index=[1])
    prediction = pipe.predict(data_df)

    return jsonify({'prediction': list(prediction)})

"""
Running flask online using docker container on Heroku

"""    

if __name__ == '__main__':
  
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)



