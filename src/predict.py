import joblib
import pandas as pd

model = joblib.load("models/loan_model.pkl")

sample_data = pd.DataFrame({
    "Gender":["Male"],
    "Married":["Yes"],
    "Dependents":["1"],
    "Education":["Graduate"],
    "Self_Employed":["No"],
    "ApplicantIncome":[5000],
    "CoapplicantIncome":[2000],
    "LoanAmount":[150],
    "Loan_Amount_Term":[360],
    "Credit_History":[1.0],
    "Property_Area":["Urban"]
})

prediction = model.predict(sample_data)

probability = model.predict_proba(sample_data)

print("Prediction:", prediction[0])

print(
    "Approval Probability:",
    round(probability[0][1] * 100, 2),
    "%"
)