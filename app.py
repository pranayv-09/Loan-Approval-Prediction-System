import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/loan_model.pkl")

# Page Config
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Loan Approval Prediction System")
st.info(
    "Machine Learning based Loan Approval Prediction System"
)
st.caption(
    "Built using Logistic Regression, Scikit-Learn and Streamlit"
)
st.caption(
    "Built by Pranay Verma | Logistic Regression | Streamlit"
)
st.markdown(
    "Enter applicant details below to predict whether the loan will be approved."
)

st.divider()

# Inputs

gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["Yes", "No"])

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=150
)

loan_term = st.number_input(
    "Loan Amount Term",
    min_value=0,
    value=360
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

# Predict Button

if st.button("Predict Loan Status"):

    input_df = pd.DataFrame({
        "Gender": [gender],
        "Married": [married],
        "Dependents": [dependents],
        "Education": [education],
        "Self_Employed": [self_employed],
        "ApplicantIncome": [applicant_income],
        "CoapplicantIncome": [coapplicant_income],
        "LoanAmount": [loan_amount],
        "Loan_Amount_Term": [loan_term],
        "Credit_History": [credit_history],
        "Property_Area": [property_area]
    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    st.progress(float(probability))
    st.metric(
    label="Approval Probability",
    value=f"{probability:.2%}"
)

    if prediction == "Y":
        st.success(
            f"✅ Loan Approved\n\nApproval Probability: {probability:.2%}"
        )
    else:
        st.error(
            f"❌ Loan Rejected\n\nApproval Probability: {probability:.2%}"
        )