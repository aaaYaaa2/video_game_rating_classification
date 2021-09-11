from flask import Flask, jsonify, request 
import joblib
app = Flask(__name__)

def load_joblib_model(self, joblib_filename: str):
    model = joblib.load(joblib_filename)
    return model 

@app.route("/predict")

def predict(model):
    input_example = request.args.get("input")
    output = model.predict(input_example)
    return jsonify(output)



