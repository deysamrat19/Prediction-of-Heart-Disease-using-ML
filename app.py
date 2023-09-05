# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

heart_disease_model = pickle.load(open('C:/Users/Anwayajyoti Dey/OneDrive/Desktop/Project Presentation/heart_disease_prediction.sav','rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          ['Heart Disease Prediction',
                           'Details in Brief'],
                          icons=['heart','bag-plus'],
                          default_index=0)
    

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.selectbox('Sex' , (0,1))
        
    with col3:
        cp = st.selectbox('Chest Pain types' , (0,1,2,3))
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar',(0,1))
        
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results',(0,1,2))
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina',(0,1))
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment',(0,1,2))
        
    with col3:
        ca = st.selectbox('Major vessels colored by flourosopy',(0,1,2,3,4))
        
    with col1:
        thal = st.selectbox('thal',(0,1,2,3))
        
      
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
# Details Page
if (selected == 'Details in Brief'):
    
    #page title
    st.title('Details about the different Parametes Used')
    st.write("=> age - age in years")
    st.write("=> sex - (1 = male; 0 = female)")
    st.write("=> cp - chest pain type")
    st.write("0: Typical angina: chest pain related decrease blood supply to the heart")
    st.write("1: Atypical angina: chest pain not related to heart")
    st.write("2: Non-anginal pain: typically esophageal spasms (non heart related)")
    st.write("3: Asymptomatic: chest pain not showing signs of disease")
    st.write("=> trestbps - resting blood pressure (in mm Hg on admission to the hospital) anything above 130-140 is typically cause for concern")
    st.write("=> chol - serum cholestoral in mg/dl) above 200 is cause for concern")
    st.write("=> fbs - (fasting blood sugar) (1 = true; 0 = false)")
    st.write("=> restecg - resting electrocardiographic results")
    st.write("0: Nothing to note")
    st.write("1: ST-T Wave abnormality")
    st.write("can range from mild symptoms to severe problems")
    st.write("signals non-normal heart beat")
    st.write("2: Possible or definite left ventricular hypertrophy")
    st.write("Enlarged heart's main pumping chamber")
    st.write("=> thalach - maximum heart rate achieved")
    st.write("=> exang - exercise induced angina (1 = yes; 0 = no)")
    st.write("=> oldpeak - ST depression induced by exercise relative to rest looks at stress of heart during excercise unhealthy heart will stress more")
    st.write("=> slope - the slope of the peak exercise ST segment")
    st.write("0: Upsloping: better heart rate with excercise (uncommon)")
    st.write("1: Flatsloping: minimal change (typical healthy heart)")
    st.write("2: Downslopins: signs of unhealthy heart")
    st.write("=> ca - number of major vessels (0-4) colored by flourosopy")
    st.write("=> thal - thalium stress result")
    st.write("0: normal")
    st.write("1: fixed defect: used to be defect but ok now")
    st.write("2: reversable defect: no proper blood movement when excercising")
