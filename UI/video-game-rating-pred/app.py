from flask import Flask 
from flask import request 
from flask import make_response
import joblib
import pandas as pd 
import numpy as np 
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST', 'GET', 'OPTIONS'])

def transform_req_to_df():
    cur_features = [
        'console', 
        'alcohol_reference', 
        'animated_blood', 
        'blood',
        'blood_and_gore', 
        'cartoon_violence',
        'drug_reference',
        'fantasy_violence',
        'intense_violence',
        'mature_humor',
        'mild_fantasy_violence',
        'mild_lyrics',
        'mild_suggestive_themes',
        'sexual_content',
        'sexual_themes',
        'simulated_gambling',
        'strong_janguage',
        'strong_sexual_content',
        'suggestive_themes',
        'use_of_drugs_and_alcohol'
    ]

    formData = json.loads(request.get_data())['form']
    data_arr = []

    if request.method == 'POST' or request.method == 'OPTIONS':
        for i in range(len(cur_features)):
            print(formData['alcohol_reference'] != None)
            if formData[cur_features[i]] != None:
                cur_val = 1 if formData[cur_features[i]] else 0
                data_arr.append(cur_val)
            else:
                error = 'There are missing features in your request, ' + cur_features[i]
                return error
        test_df = pd.DataFrame(np.array([data_arr]), columns=cur_features)
        old_model = joblib.load('../../DECISION_TREES_model.joblib')
        pred = pd.Series(old_model.predict(test_df))
        response = make_response(json.dumps({'result': str(pred[0])}), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        print(response.get_data())
        return response
    else:
        return 'This is the GET method.'

