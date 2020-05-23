from flask import Flask, render_template, url_for, request, jsonify, make_response
import text_api
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/predict/", methods=['GET','POST'])
def api():
    if request.method == 'GET':
        return make_response(jsonify({ 'message': 'This has no endpoint for GET request' }), 200)

    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        smoker = request.form.get('smoker')
        symptoms = request.form.getlist('reported_symptoms')
        medical_history = request.form.getlist('medical_history')
        response = {"age": int(age), "gender": gender,
        "smoker": smoker, "patient_reported_symptoms": symptoms,
        "medical_history": medical_history}
        # print(response)
        symptoms = ",".join(symptoms)
        medical_history = ",".join(medical_history)
        response = {"age": int(age), "gender": gender,
        "smoker": smoker, "patient_reported_symptoms": symptoms,
        "medical_history": medical_history}
        # print(response)
        df1 = pd.DataFrame(response,index=[0])
        df1 = df1.replace('NaN',np.NaN)
        prediction = text_api.predict(df1,"textual_model83.sav")
        print("prediction is: ",prediction)
        return make_response(jsonify({"data":round(prediction,3)}), 200)