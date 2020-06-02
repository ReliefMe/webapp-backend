from flask import Flask, render_template, url_for, request, jsonify, make_response
from sklearn.externals import joblib
import text_api
from werkzeug import *
import pandas as pd
import numpy as np
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    dicti = data()
    return render_template('app.html',predic=dicti)
        

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        try: 
            age = request.form.get('age')
            gender = request.form.get('gender')
            smoker = request.form.get('smoker')
            cough_audio = request.files["cough_audio"]
            symptoms = request.form.getlist('reported_symptoms')
            # filePath = "/home/naufil/Desktop/reliefme/webapp-backend/" + cough_audio.filename
            # print(filePath)
            cough_audio.save(filePath)
            medical_history = request.form.getlist('medical_history')
            symptoms = ",".join(symptoms) + ","
            medical_history = ",".join(medical_history) + ","
            response = {"age": [int(age)], "gender": [gender],
            "smoker": [smoker], "patient_reported_symptoms": [symptoms],
            "medical_history": [medical_history]
            }
            df1 = pd.DataFrame(response)
            # print(df1)
            prediction = text_api.predict(df1, "./model81.pkl")
            if prediction[0] == 0:
                return "Great, you are out of danger according to our model keep following precautions."
            else:
                return "You are at risk according to our model, consult a doctor and keep yourself away from others."

        except:
             return "Please check if the values are entered correctly"
    
app.run(debug=True)




