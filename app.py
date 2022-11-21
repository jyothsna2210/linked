# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:16:21 2022

@author: Jyothsna
""" 

import numpy as np
import pickle
import streamlit  as st
loaded_model=pickle.load(open("C:\Users\Jyothsna\OneDrive\Desktop\hernok\trained_mode.sav",'rb'))
def diabetics_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction==[0]):
     return 'the person is not diabetic'
    else:
      return 'the person is diabetic'
def main():

    st.title('Diabetics prediction web app')
    Pregnancies=st.text_input("NO OF  Pregnancies")
    Glucose=st.text_input("NO OF Glucose ")
    BloodPressure=st.text_input("NO OF  bloodPressure")
    SkinThickness=st.text_input("NO OF  SkinThickness")
    Insulin=st.text_input("NO OF  Insulin")
    BMI=st.text_input("NO OF  SBMI")
    DiabetesPedigreeFunction=st.text_input("NO OF  DiabetesPedigreeFunction")
    Age=st.text_input("NO OF  Age")
    diagnosis=''
    if st.button('Diabetics test result'):
        diagnosis=diabetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success( diagnosis)
if __name__ == '__main__':
    main()
