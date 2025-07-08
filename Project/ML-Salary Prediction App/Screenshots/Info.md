# OP-1 :- Initial Interface (Before Prediction)
  - The user is presented with a clean UI titled "Salary Prediction App".
  - A slider/input box allows the user to enter Years of Experience (default: 1.00).
  - A "Predict Salary" button is shown below.
  - No prediction is visible yet because the user hasn’t clicked the button.

# OP-2 :-  Prediction for 1.0 Year of Experience
  - After entering 1.00 as experience and clicking "Predict Salary",
  - The model predicts a salary of $36,092.67.
  - This result is shown inside a green success message box using st.success().
  - This demonstrates that even low experience can yield a prediction based on the trained model.

# OP-3 :- Prediction for 20.0 Years of Experience
  - Input: 20.00 years of experience
  - Predicted salary: $213,031.60
  - This shows that as experience increases, the predicted salary increases linearly, which is expected behavior in Simple Linear Regression.










