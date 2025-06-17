# sleep_app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Sleep Disorder Prediction Tool")
st.markdown("Enter your health and lifestyle details below to predict potential sleep disorders.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 80, 30)
bmi_category = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
sleep_duration = st.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
quality_sleep = st.slider("Quality of Sleep (1–10)", 1, 10, 6)
physical_activity = st.slider("Physical Activity Level (1–10)", 0, 10, 5)
stress_level = st.slider("Stress Level (1–10)", 1, 10, 6)
heart_rate = st.slider("Heart Rate (bpm)", 40, 150, 70)
systolic = st.slider("Systolic BP", 90, 200, 120)
diastolic = st.slider("Diastolic BP", 60, 140, 80)
occupation = st.selectbox("Occupation", ["Nurse", "Doctor", "Engineer", "Teacher", "Salesperson", "Accountant", "Lawyer", "Others"])

# Put into DataFrame
input_df = pd.DataFrame({
    'Gender': [gender],
    'Age': [age],
    'BMI Category': [bmi_category],
    'Sleep Duration': [sleep_duration],
    'Quality of Sleep': [quality_sleep],
    'Physical Activity Level': [physical_activity],
    'Stress Level': [stress_level],
    'Heart Rate': [heart_rate],
    'Systolic': [systolic],
    'Diastolic': [diastolic],
    'Occupation': [occupation]
})

# TO DO: Apply preprocessing steps if needed here, e.g., one-hot encoding (same as your training process)

# Predict button
if st.button("Predict Sleep Disorder"):
    prediction = model.predict(input_df)[0]
    st.success(f"Prediction: **{prediction}**")

    if prediction == "Insomnia":
        st.info("💡 Recommendation: Try relaxation techniques and improve your sleep schedule.")
    elif prediction == "Sleep Apnea":
        st.warning("⚠️ Recommendation: You may need to see a sleep specialist for diagnosis.")
    else:
        st.balloons()
        st.success("✅ You are not likely experiencing a sleep disorder.")
