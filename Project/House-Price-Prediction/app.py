from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os

app = Flask(__name__)

# List of model names
model_names = [
    'LinearRegression', 'RobustRegression', 'RidgeRegression', 'LassoRegression', 'ElasticNet',
    'PolynomialRegression', 'SGDRegressor', 'ANN', 'RandomForest', 'SVM', 'LGBM',
    'XGBoost', 'KNN'
]

# Load models into a dictionary
models = {}
for name in model_names:
    model_path = f"{name}.pkl"
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            models[name] = pickle.load(f)
    else:
        print(f"⚠ Warning: {model_path} not found. Skipping...")

# Load evaluation results if available
results_df = None
if os.path.exists('model_evaluation_results.csv'):
    results_df = pd.read_csv('model_evaluation_results.csv')
else:
    print("⚠ Warning: model_evaluation_results.csv not found.")

@app.route('/')
def index():
    return render_template('index.html', model_names=model_names)

@app.route('/predict', methods=['POST'])
def predict():
    model_name = request.form.get('model')

    try:
        input_data = {
            'Avg. Area Income': float(request.form.get('Avg. Area Income')),
            'Avg. Area House Age': float(request.form.get('Avg. Area House Age')),
            'Avg. Area Number of Rooms': float(request.form.get('Avg. Area Number of Rooms')),
            'Avg. Area Number of Bedrooms': float(request.form.get('Avg. Area Number of Bedrooms')),
            'Area Population': float(request.form.get('Area Population'))
        }
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input values'}), 400

    input_df = pd.DataFrame([input_data])

    if model_name in models:
        model = models[model_name]
        prediction = model.predict(input_df)[0]
        return render_template(
            'results.html',
            prediction=round(prediction, 2),
            model_name=model_name
        )
    else:
        return jsonify({'error': 'Model not found'}), 400

@app.route('/results')
def results():
    if results_df is not None:
        return render_template(
            'model.html',
            tables=[results_df.to_html(classes='data', index=False)],
            titles=results_df.columns.values
        )
    else:
        return "No evaluation results available."

if __name__ == '__main__':
    # Avoid SIGTERM crash on Python 3.13 by disabling auto-reloader
    app.run(debug=True, use_reloader=False)
