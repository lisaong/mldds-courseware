import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

# Read data
df = pd.read_csv('auto-mpg.data-nans.txt',
                 delim_whitespace=True, # the data uses whitespaces as separators instead of commas
                 na_values=['?', 'NA'],  # to handle '?' in the horsepower column
                 names=['mpg', 'cylinders', 'displacement', 'horsepower', # data has no column names
                        'weight', 'acceleration', 'model_year', 'origin', 'car_name'])

# This returns a view, so we can call it again without resulting in a copy of the data
input_X = df.loc[:, 'cylinders':'origin']

# Load scaler from pickle
X_scaler = pickle.load(open('X_scaler.sav', 'rb'))
y_scaler = pickle.load(open('y_scaler.sav', 'rb'))

model = pickle.load(open('model.sav', 'rb'))

input_X_scaled = X_scaler.transform(input_X)

output_scaled = model.predict(input_X_scaled)
output = y_scaler.inverse_transform(output_scaled)

print(input_X)
print(output)