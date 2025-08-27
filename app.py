import streamlit as st
import pickle
import numpy as np

# load trained model

with open("trained_model.sav", "rb") as file:
    model = pickle.load(file)

st.markdown("<h2 style='color: blue; text-align: center;'>Heart Disease Prediction App</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(['Predict','Bulk Predict','Model Information'])

with tab1:
    age = st.number_input("Age(years)",min_value=0, max_value=150)
    sex = st.selectbox("Sex",["Male","Female"])
    cp = st.number_input("Chest Pain Type (1-4)",min_value=1, max_value=4, value=2)
    trestbps = st.number_input("Resting Blood Pressure",min_value=80, max_value=200,value=120)
    chol = st.number_input("Cholesterol",min_value=100, max_value=600,value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",(0,1))
    restecg = st.number_input("Resting ECG(0-2)",min_value=0, max_value=2, value=1)
    thalach = st.number_input("Maximum Heart rate Achieved",min_value=60,max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina",(0,1))
    oldpeak = st.number_input("Oldpeak (ST Depression)",min_value=0.0, max_value=10.0, step=0.1)
    slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0,max_value=2,value=1)
   
# Predict Button
if st.button(" Predict"):
    input_data = np.array([[age,
                            1 if sex == "Male" else 0,
                            cp, trestbps, chol, fbs,
                            restecg, thalach,exang,
                            oldpeak,slope ]])
    #input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction =model.predict(input_data)

    # Show result
    if prediction[0] == 0:
        st.markdown("<h3 style='color: green;'>✅ The Person is free from Heart Disease</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: red;'>⚠️ The Person may have Heart Disease</h3>", unsafe_allow_html=True)


