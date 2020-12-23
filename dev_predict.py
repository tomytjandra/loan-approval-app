import joblib
import pandas as pd

model = joblib.load("models/loan_model_logreg.pkl")

gender = 'Male' # levels: ['Male', 'Female']
married = 'No' # levels: ['No', 'Yes']
dependents = '3+' # levels: ['0', '1', '2', '3+']
education = 'Graduate' # levels: ['Not Graduate', 'Graduate']
self_employed = 'No' # levels: ['No', 'Yes']
applicant_income = 1000 # unit: dollar
coapplicant_income = 500 # unit: dollar
loan_amount = 400 # unit: dollar
loan_amount_term = 60 # unit: days
credit_history = 1.0 # levels: ['0', '1'] -> ['Not paid', 'All debts paid']
property_area = 'Urban' # ['Rural', 'Semiurban', 'Urban']

new_data = pd.DataFrame([{
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area': property_area
}])

print(model.predict_proba(new_data)[0])