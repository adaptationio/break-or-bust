# Load libraries
import flask
import pandas as pd
import time
import gym
import numpy as np
import os
import datetime
import csv
import argparse
from functools import partial
from flask import request
from flask import make_response
from flask import jsonify
from flask_cors import CORS

import json

from stable_baselines.common.policies import MlpLnLstmPolicy, FeedForwardPolicy, LstmPolicy, CnnPolicy
from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv,VecNormalize 
from stable_baselines.common import set_global_seeds
from stable_baselines import ACKTR, PPO2
from stable_baselines.deepq import DQN
from ..env import BustaBitSim
from ..agents.policy import *
from ..agents import PPO2_SB
timestamp = datetime.datetime.now().strftime('%y%m%d%H%M%S')

# instantiate flask 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)

# we need to redefine our metric function in order 
# to use it when loading the model 
#def auc(y_true, y_pred):
    #auc = tf.metrics.auc(y_true, y_pred)[1]
    #keras.backend.get_session().run(tf.local_variables_initializer())
    #return auc

# load the model, and pass in the custom metric function
#global graph
#graph = tf.get_default_graph()
#model = load_model('games.h5', custom_objects={'auc': auc})
env_id = "default"
num_e = 1  # Number of processes to use
ppo = PPO2_SB()
env = SubprocVecEnv([ppo.make_env(env_id, i) for i in range(num_e)])
env = VecNormalize(env, norm_obs=True, norm_reward=True)
env.live = True
#env.action_dim = 2
#env.observation_space = spaces.Box(low=-1000, high=1000, shape=(2,))
model = PPO2.load('saves/agent4.pkl', env, policy=CustomPolicy, tensorboard_log="./ppocnn/" )
obs = []
count = 0
# adding my shit
#obs = env.reset()
# define a predict function as an endpoint 
@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    global count
    global obs
    global actions
    global rewards

    #params = flask.request.json
    if request.is_json:
        # Parse the JSON into a Python dictionary
        req = request.get_json()
        state = req.get("gamearray")
        state = json.dumps(state)
        state = json.loads(state)
        # Print the dictionary
        
        #x=pd.DataFrame.from_dict(params, orient='index').transpose()
        #with graph.as_default():
        #data["prediction"] = str('moose')
        #data["success"] = True
        #data = 'itworked'
        state = np.array(state)
        if count == 0:
            env.live_state = state
            obs = env.reset()
            actions, _states = model.predict(obs)
            
        else:
            env.live_state = state
            
        
            # # here, action, rewards and dones are arrays
            # # because we are using vectorized env
        
        obs, rewards, dones, info = env.step(actions)
        actions, _states = model.predict(obs)
        print(actions)
        #print(params)
        #response = flask.jsonify(data)
        #response.headers.add('Access-Control-Allow-Origin', '*')
        #response.header.add('Content-Type', 'application/json')
        #response.headers.add("Access-Control-Allow-Credentials", True )
        response_body = {
            "action": str(actions[0])
            #"sender": req.get("name")
        }
        res = make_response(jsonify(response_body), 200)
        res.headers.add('Access-Control-Allow-Origin', '*')
        res.headers.add("Access-Control-Allow-Methods", "POST")
        res.headers.add("Access-Control-Allow-Headers", "Content-Type")
        
        count += 1
        return res
    else:
        #(params == None):
        #params = flask.request.args
        data["prediction"] = str('moose')
        data["success"] = False
        #response = flask.jsonify(data)
        #response.headers.add('Access-Control-Allow-Origin', '*')
        #response.header.add('Content-Type', 'application/json')

        res = make_response(jsonify({"message": "Request body must be JSON"}), 400)
        res.headers.add('Access-Control-Allow-Origin', '*')
        res.headers.add("Access-Control-Allow-Methods", "POST")
        res.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return res
        
    # if parameters are found, return a prediction
    
        


    # return a response in json format 
    #return response   
#openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# start the flask app, allow remote connections 
#
#chrome://flags/#allow-insecure-localhost

#app.run(ssl_context=('cert.pem', 'key.pem'), host='localhost')

#@app.route("/json", methods=["POST"])
#def json_example():

    # Validate the request body contains JSON
    #if request.is_json:

        # Parse the JSON into a Python dictionary
        #req = request.get_json()

        # Print the dictionary
        #print(req)

        # Return a string along with an HTTP status code
        #return "JSON received!", 200

    #else:

        # The request body wasn't JSON so return a 400 HTTP status code
        #return "Request was not JSON", 400
#def json_example():

    #if request.is_json:

        #req = request.get_json()

        #response_body = {
            #"message": "JSON received!",
            #"sender": req.get("name")
        #}

        #res = make_response(jsonify(response_body), 200)

        #return res

    #else:

        #return make_response(jsonify({"message": "Request body must be JSON"}), 400)