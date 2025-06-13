from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('boston_model.pkl', 'rb'))

# Feature names
FEATURES = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features and make prediction
    features = [float(request.form[f]) for f in FEATURES]
    prediction = model.predict(np.array(features).reshape(1, -1))[0]
    
    # Format prediction and return with feature values
    result = {"prediction": f"${prediction:.2f}K"}
    result.update({f: features[i] for i, f in enumerate(FEATURES)})
    
    return render_template('index.html', **result)

if __name__ == '__main__':
    print("Boston House Price Prediction App - Running on http://localhost:5000")
    app.run(debug=True)
