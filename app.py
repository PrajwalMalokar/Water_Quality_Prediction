import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("D:/AICTE Internship1/Water-Quality-Prediction/svm.pkl")


# Streamlit App Title
st.title("Water Quality Prediction App")
st.write("Enter the water quality parameters to predict whether the water is Safe or Unsafe.")

# Input fields for user to enter values
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=100.0)
solids = st.number_input("Solids", min_value=0.0, value=5000.0)
chloramines = st.number_input("Chloramines", min_value=0.0, value=5.0)
sulfate = st.number_input("Sulphate", min_value=0.0, value=250.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=300.0)
organicCarbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=50.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=5.0)

# Predict button
if st.button("Predict Water Quality"):
    input_values = [ph, hardness, solids, chloramines, sulfate, conductivity, organicCarbon, trihalomethanes, turbidity]
    prediction = model.predict([input_values])[0]
    
    prediction_text = "Safe" if prediction == 1 else "Unsafe"
    st.write(f"The predicted water quality is: **{prediction_text}**")
