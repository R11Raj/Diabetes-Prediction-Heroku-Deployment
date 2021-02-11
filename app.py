# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:32:38 2020

@author: Raj
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    f=open('test.txt','w')
    f.write('dvsdvsvsdvsdvsdvsdv')
    f.close()
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output=''
    f=open('test.txt','r')
    
    if prediction:
        output=f.read()+"You have Diabetes , Please Take of care of Yourself"
    else:
        output=f.read()+"You don't have Diabetes , Enjoy your life but don't be overconfident about your food choices"

    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True)