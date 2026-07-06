import streamlit as st
from utils import PrepProcesor, columns 
import os
import numpy as np
import pandas as pd
import skops.io as sio

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.skops')

if not os.path.exists(MODEL_PATH):
    st.stop()

@st.cache_resource
def load_model():
    try:
        unknown_types = sio.get_untrusted_types(file=MODEL_PATH)
        print(f"انواع ناشناخته: {unknown_types}")
        model = sio.load(MODEL_PATH, trusted=unknown_types)
        return model
    except Exception as e:
        st.error(f"{e}")
        st.stop()

model = load_model()

st.title('Titanic Survival or Not( made by Pooya Valizadeh)')
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
passengerid = st.text_input("ID", '2626') 
pclass = st.selectbox("class", [1,2,3])
name  = st.text_input("Passenger Name", 'Pooya Valizadeh')
sex = st.selectbox("sex", ['male','female'])
age = st.slider("age",0,100)
sibsp = st.slider("siblings",0,10)
parch = st.slider("parch",0,10)
ticket = st.text_input("Ticket Number", "2626") 
fare = st.number_input("Fare Price", 0,1000)
cabin = st.text_input("Cabin", "C26") 
embarked = st.select_slider("Embark?", ['S','C','Q'])

def predict(): 
    row = np.array([passengerid,pclass,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('Passenger Survived (:')
    else: 
        st.error('Passenger did not Survive :(') 

trigger = st.button('Predict', on_click=predict)

