# -*- coding: utf-8 -*-
"""
Created on Fri May 19 00:52:11 2023

@author: HP
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class model_input(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int
    
diabetes_model=pickle.load(open('D:/ML projects/Multiple diesease api/diabetes_model.sav','rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    preg=input_dictionary['Pregnancies']
    gluc=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    st=input_dictionary['SkinThickness']
    insu=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    
    input_list=[preg,gluc,bp,st,insu,bmi,dpf,age]
    prediction=diabetes_model.predict([input_list])
    
    if(prediction[0]==0):
        return 'Person is not diabetic'
    else:
        return 'Person in diabetic'