# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 09:01:53 2023

@author: SUNOJ CH
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

lung_cancer_model = pickle.load(open('lungcancer_model.sav', 'rb'))



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
        GENDER = st.text_input('Gender')
        
    with col2:
        AGE = st.text_input('Age')
    
    with col3:
        SMOKING = st.text_input('Smoking')
    with col4:
        YELLOW_FINGERS = st.text_input('Yellow Fingers')
        
    with col5:
        ANXIETY = st.text_input('Anxiety')
    
    with col1:
        PEER_PRESSURE = st.text_input('Peer Pressure')
    with col2:
        CHRONIC_DISEASE = st.text_input('Chronic Disease')
        
    with col3:
        FATIGUE = st.text_input('Fatigue')
    
    with col4:
        ALLERGY = st.text_input('Allergy')
    with col5:
        WHEEZING = st.text_input('Wheezing')
        
    with col1:
        ALCOHOL_CONSU1ING = st.text_input('Alcohol Consuming')
        
    with col2:
        COUGHING = st.text_input('Coughing')
    
    with col3:
        SHORTNESS_OF_BREATH = st.text_input('Shortness of Breath')
        
    with col4:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing Difficulty')
        
    with col5:
        CHEST_PAIN = st.text_input('Chest Pain')
        
        # code for Prediction
    lung_cancer = ""
    
    # creating a button for Prediction
    
    if st.button('Lung Cancer Test Result'):
        lung_prediction = lung_cancer_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL_CONSU1ING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        
        if (lung_prediction[0] == 1):
          lung_diagnosis = 'The person is having Lung Cancer'
            
          lung_diagnosis = 'The person is diabetic'
        else:
          lung_diagnosis = 'The person is not having Lung Cancer'
        
    st.success(lung_cancer)
    
   
    
  
    
    
    
    
        
    
    
