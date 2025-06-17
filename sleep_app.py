import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Expected columns based on model training
expected_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                 'Stress Level', 'Heart Rate', 'Daily Steps', 'Systolic', 'Diastolic',
                 'Gender_Male',
                 'Occupation_Doctor', 'Occupation_Engineer', 'Occupation_Lawyer',
                 'Occupation_Manager', 'Occupation_Nurse', 'Occupation_Sales Representative',
                 'Occupation_Salesperson', 'Occupation_Scientist', 'Occupation_Software Engineer',
                 'Occupation_Teacher',
                 'BMI Category_Obese', 'BMI Category_Overweight']

st.title("Sleep Disorder Prediction Tool")
st.markdown("Enter your health and lifestyle details to predict potential sleep disorders.")

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
occupation = st.selectbox("Occupation", [
    "Doctor", "Engineer", "Lawyer", "Manager", "Nurse", "Sales Representative",
    "Salesperson", "Scientist", "Software Engineer", "Teacher"
])

# Prepare raw input
raw_input = {
    'Age': age,
    'Sleep Duration': sleep_duration,
    'Quality of Sleep': quality_sleep,
    'Physical Activity Level': physical_activity,
    'Stress Level': stress_level,
    'Heart Rate': heart_rate,
    'Daily Steps': 0,  # Replace with real value if used
    'Systolic': systolic,
    'Diastolic': diastolic,
    'Gender_Male': 1 if gender == "Male" else 0,
    f'Occupation_{occupation}': 1,
    f'BMI Category_{bmi_category}': 1
}

# Convert to DataFrame
X_input = pd.DataFrame([raw_input])

# Ensure all expected columns are present (fill missing with 0)
for col in expected_cols:
    if col not in X_input.columns:
        X_input[col] = 0

# Reorder to match training set
X_input = X_input[expected_cols]

# Prediction
if st.button("Predict Sleep Disorder"):
    prediction = model.predict(X_input)[0]
    st.success(f"Prediction: **{prediction}**")

    if prediction == "Insomnia":
        st.info("💡 Try relaxation techniques and improve your sleep hygiene.")
    elif prediction == "Sleep Apnea":
        st.warning("⚠️ Consider visiting a sleep clinic for further testing.")
    else:
        st.balloons()
        st.success("✅ You are not likely experiencing a sleep disorder.")
