# Sleep Disorder Predictor

A machine learning project that predicts sleep disorders (Insomnia, Sleep Apnea or None) from health and lifestyle data, deployed as an interactive Streamlit web app.

## Overview
- Performed exploratory data analysis (EDA) to find key drivers of sleep disorders, such as BMI, blood pressure and stress level
- Built a Random Forest classifier tuned with GridSearchCV
- Achieved **88% accuracy** across 3 classes
- Deployed the model as a Streamlit app where users enter their lifestyle details to get an instant prediction

## Dataset
[Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) (Kaggle): 374 records, 13 features including sleep duration, stress level, BMI category, blood pressure, heart rate and daily steps.

## Tech Stack
Python · Pandas · scikit-learn · Matplotlib · Seaborn · Streamlit

## Files
| File | Description |
|---|---|
| `sleep_disorder_prediction.ipynb` | Data cleaning, EDA and model training |
| `sleep_app.py` | Streamlit web app |
| `model.pkl` | Trained Random Forest model |
| `Sleep_health_and_lifestyle_dataset.csv` | Dataset |
| `requirements.txt` | Python dependencies |

## Run Locally
```
pip install -r requirements.txt
streamlit run sleep_app.py
```
