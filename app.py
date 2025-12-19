import streamlit as st
import numpy as np
import joblib

model = joblib.load("diabetes_model.pkl")

st.title("🩺 Diabetes Prediction Tool")

preg = st.number_input("Pregnancies", 0)
glucose = st.number_input("Glucose Level", 0)
bp = st.number_input("Blood Pressure", 0)
skin = st.number_input("Skin Thickness", 0)
insulin = st.number_input("Insulin", 0)
bmi = st.number_input("BMI", 0.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0)
age = st.number_input("Age", 0)

if st.button("Predict"):
    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("⚠️ Likely Diabetic")
    else:
        st.success("✅ Not Diabetic")

st.caption("For educational purposes only")
    