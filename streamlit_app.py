# import streamlit as st
# import pandas as pd
# import joblib

# # Load the pre-trained LightGBM model using joblib
# # model = joblib.load('HarshitModel.joblib')
# model = joblib.load('webappmodel.joblib')

# # Create a function to predict using the model
# def predict_default_probability(features):
#     prediction = model.predict(features)
#     return prediction

# # Create the web app UI
# st.title("Credit Default Prediction App")
# st.write("Enter customer information to predict credit default probability:")

# # Collect user input
# revolving_utilization = st.number_input("Revolving Utilization of Unsecured Lines")
# age = st.number_input("Age")
# num_30_59_past_due = st.number_input("Number of Times 30-59 Days Past Due")
# debt_ratio = st.number_input("Debt Ratio")
# monthly_income = st.number_input("Monthly Income")
# num_credit_lines_loans = st.number_input("Number of Open Credit Lines and Loans")
# num_90_days_late = st.number_input("Number of Times 90 Days Late")
# num_real_estate_loans = st.number_input("Number of Real Estate Loans or Lines")
# num_60_89_past_due = st.number_input("Number of Times 60-89 Days Past Due")
# num_dependents = st.number_input("Number of Dependents")

# # Create a button to trigger prediction
# if st.button("Predict"):
#     # Create the input_data DataFrame with the correct features
#     input_data = pd.DataFrame({
#         'RevolvingUtilizationOfUnsecuredLines': [revolving_utilization],
#         'age': [age],
#         'NumberOfTime30-59DaysPastDueNotWorse': [num_30_59_past_due],
#         'DebtRatio': [debt_ratio],
#         'MonthlyIncome': [monthly_income],
#         'NumberOfOpenCreditLinesAndLoans': [num_credit_lines_loans],
#         'NumberOfTimes90DaysLate': [num_90_days_late],
#         'NumberRealEstateLoansOrLines': [num_real_estate_loans],
#         'NumberOfTime60-89DaysPastDueNotWorse': [num_60_89_past_due],
#         'NumberOfDependents': [num_dependents]
#     })

#     # Print the input data for debugging
#     st.write("Input Data:")
#     st.write(input_data)

#     prediction = predict_default_probability(input_data)[0]

#     st.write(f"Predicted Default Probability: {prediction:.2f}")


import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained LightGBM model using joblib
# model = joblib.load('HarshitModel.joblib')
model = joblib.load('webappmodel.joblib')

# Create a function to predict using the model
def predict_default_probability(features):
    prediction = model.predict(features)
    return prediction

# Create the web app UI
st.title("Credit Default Prediction App")
st.write("Enter customer information to predict credit default probability:")

# File uploader for user's CSV file
st.sidebar.header("Upload your own CSV file")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Initialize user_data as None
user_data = None

# If a file is uploaded, read it as a DataFrame and store it in user_data
if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded successfully")

# Collect user input
revolving_utilization = st.number_input("Revolving Utilization of Unsecured Lines")
age = st.number_input("Age")
num_30_59_past_due = st.number_input("Number of Times 30-59 Days Past Due")
debt_ratio = st.number_input("Debt Ratio")
monthly_income = st.number_input("Monthly Income")
num_credit_lines_loans = st.number_input("Number of Open Credit Lines and Loans")
num_90_days_late = st.number_input("Number of Times 90 Days Late")
num_real_estate_loans = st.number_input("Number of Real Estate Loans or Lines")
num_60_89_past_due = st.number_input("Number of Times 60-89 Days Past Due")
num_dependents = st.number_input("Number of Dependents")

# Create a button to trigger prediction
if st.button("Predict"):
    if user_data is not None:
        # Use the user-uploaded data for prediction
        input_data = user_data
    else:
        # Create the input_data DataFrame with the user-entered features
        input_data = pd.DataFrame({
            'RevolvingUtilizationOfUnsecuredLines': [revolving_utilization],
            'age': [age],
            'NumberOfTime30-59DaysPastDueNotWorse': [num_30_59_past_due],
            'DebtRatio': [debt_ratio],
            'MonthlyIncome': [monthly_income],
            'NumberOfOpenCreditLinesAndLoans': [num_credit_lines_loans],
            'NumberOfTimes90DaysLate': [num_90_days_late],
            'NumberRealEstateLoansOrLines': [num_real_estate_loans],
            'NumberOfTime60-89DaysPastDueNotWorse': [num_60_89_past_due],
            'NumberOfDependents': [num_dependents]
        })

    # Print the input data for debugging
    st.write("Input Data:")
    st.write(input_data)

    prediction = predict_default_probability(input_data)[0]

    st.write(f"Predicted Default Probability: {prediction:.2f}")
