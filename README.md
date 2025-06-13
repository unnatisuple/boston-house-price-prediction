# Boston House Price Prediction

This project predicts house prices in Boston using a Linear Regression model trained on the Boston Housing Dataset. It includes a web interface built with Flask where users can input house features and get a price prediction.

## Project Structure

```
boston-house-price-prediction/
├── boston_house_price_prediction.ipynb   # Model training notebook
├── app.py                               # Flask application
├── boston_model.pkl                     # Saved model (generated from notebook)
├── requirements.txt                     # Project dependencies
└── templates/
    └── index.html                       # Web interface template
```

## Features Used for Prediction

The model uses these features from the Boston Housing Dataset:

- **CRIM**: Per capita crime rate by town
- **ZN**: Proportion of residential land zoned for large lots
- **INDUS**: Proportion of non-retail business acres per town
- **CHAS**: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- **NOX**: Nitric oxides concentration (parts per 10 million)
- **RM**: Average number of rooms per dwelling
- **AGE**: Proportion of owner-occupied units built prior to 1940
- **DIS**: Weighted distances to five Boston employment centers
- **RAD**: Index of accessibility to radial highways
- **TAX**: Full-value property-tax rate per $10,000
- **PTRATIO**: Pupil-teacher ratio by town
- **B**: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents
- **LSTAT**: % lower status of the population

## Quick Start Guide

### Step 1: Install dependencies
```
pip install -r requirements.txt
```

### Step 2: Train the model
Run the Jupyter notebook to train the model and create the pickle file:
```
jupyter notebook boston_house_price_prediction.ipynb
```
- Open the notebook in your browser
- Run all cells by clicking "Run All" in the "Cell" menu or by pressing Shift+Enter on each cell
- This creates the `boston_model.pkl` file needed for the web app

### Step 3: Start the Flask app
```
python app.py
```

### Step 4: Open the web interface
Open your browser and go to:
```
http://localhost:5000
```

That's it! You can now enter housing features and get price predictions.

## Troubleshooting

- **Missing dependencies**: Make sure you've activated your virtual environment and installed all dependencies.
- **Model not found**: Ensure you've run the Jupyter notebook completely to generate the model file.
- **Port already in use**: If port 5000 is occupied, modify the line `app.run(debug=True)` in app.py to use a different port.

## Model Performance

- **Mean Squared Error (MSE)**: Measures the average squared difference between predicted and actual values
- **Root Mean Squared Error (RMSE)**: Square root of MSE, gives error in the same units as the target variable
- **R-squared (R²)**: Indicates how well the model fits the data (higher is better)

Check the notebook for detailed performance metrics and analysis.
