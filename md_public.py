# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 09:01:53 2023

@author: SUNOJ CH
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

lung_cancer_model = pickle.load(open('trained_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    

    
    selected = option_menu('Disease Prediction System',
                          
                          [
                           'Lung Cancer Prediction'],
                          icons=['Heart'],
                          default_index=0)
    
    
   
    
    # lung cancer Prediction Page
if (selected == 'Lung Cancer Prediction'):
    # page title
    st.title('Lung Cancer Prediction using ML')
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
   
    with col1:
        Gender = st.text_input('male or female')
        
    with col2:
        Age = st.text_input('Age')
    
    with col3:
        Smoking = st.text_input('Yes or No')
    with col4:
        Yellow_fingers = st.text_input('Yes or No')
        
    with col5:
        Anxiety = st.text_input('Yes or No')
    
    with col1:
        Peer_Pressure = st.text_input('Yes or No')
    with col2:
        Chronic_disease = st.text_input('Yes or No')
        
    with col3:
        Fatigue = st.text_input('Yes or No')
    
    with col4:
        Allergy = st.text_input('Yes or No')
    with col5:
        Wheezing = st.text_input('Yes or No')
        
    with col1:
        Alcohol_consuming = st.text_input('Yes or No')
        
    with col2:
         Coughing = st.text_input('Coughing')
    
    with col3:
        Shortness_of_breath = st.text_input('Yes or No')
        
    with col4:
        Swallowing_Difficulty = st.text_input('Yes or No')
        
    with col5:
        Chest_pain = st.text_input('Yes or No')
        
        # code for Prediction
    lung_cancer = ""
    
    # creating a button for Prediction
    
    if st.button('Lung Cancer Test Result'):
        lung_prediction = lung_cancer_model.predict([[Gender, Age, Smoking, Yellow_fingers, Anxiety, Peer_Pressure, Chronic_disease, Fatigue, Allergy, Wheezing, Alcohol_consuming, Coughing, Shortness_of_breath, Swallowing_Difficulty, Chest_pain]])
        
        if (lung_prediction[0] == 1):
          lung_diagnosis = 'The person is having Lung Cancer'
            
          lung_diagnosis = 'The person is diabetic'
        else:
          lung_diagnosis = 'The person is not having Lung Cancer'
        
    st.success(lung_cancer)
    
   
    
  
    
    
    
    
        
    
    