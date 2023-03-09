from flask import Flask, render_template, request 
import numpy as np
import pandas as pd
import pickle 

app = Flask(__name__)
model = pickle.load(open("model_TA.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediksi():
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
