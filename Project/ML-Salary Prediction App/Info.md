# 💼 Project 2 :-
# Salary Prediction App
  ==> A lightweight ML web app that predicts salary based on years of experience using Linear Regression.

  - 🔗 Scikit-learn for model training (Linear Regression)
  - 📦 Pickle for loading the saved model
  - 🐍 NumPy for numerical input formatting
  - 🌐 Streamlit for an interactive and minimal UI

#  Features
  - User inputs years of experience
  - Predicts salary in real-time
  - Shows clean and readable output
  - Trained on real-world salary dataset
  -  Deployed as a simple web application
# ⚙️ Actual Work (Project 2 – Salary Prediction App)
This project uses a Simple Linear Regression algorithm to predict salary based on the number of years of experience provided by the user.

🔍 How It Works:
Model Training

A dataset containing salaries and years of experience was used.

The model was trained using Linear Regression from Scikit-learn, which learns the best-fit straight line between experience and salary.

Model Saving

The trained model was saved using Pickle for reuse without retraining.

Prediction Logic

When the user enters their years of experience, the app converts it into a 2D array using NumPy and passes it to the model for prediction.

User Interface

A clean UI is built using Streamlit to take user input and display the predicted salary instantly.

# 📈 Algorithm Used:
Simple Linear Regression
It finds the relationship between one independent variable (Years of Experience) and one dependent variable (Salary) by fitting a straight line:
Salary = m × Experience + c


