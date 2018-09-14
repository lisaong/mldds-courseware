import numpy as np
import pandas as pd
import pickle
from keras.models import load_model

# Read data
df = pd.read_csv('auto-mpg.data-nans.txt',
                 delim_whitespace=True, # the data uses whitespaces as separators instead of commas
                 na_values=['?', 'NA'],  # to handle '?' in the horsepower column
                 names=['mpg', 'cylinders', 'displacement', 'horsepower', # data has no column names
                        'weight', 'acceleration', 'model_year', 'origin', 'car_name'])
print(df)

# This returns a view, so we can call it again without resulting in a copy of the data
input_X = df.loc[:, 'cylinders':'origin']

# Load scaler from pickle
X_scaler = pickle.load(open('X_scaler_keras.pickle', 'rb'))
print(X_scaler)

y_scaler = pickle.load(open('y_scaler_keras.pickle', 'rb'))
print(y_scaler)

# Load model from keras
model = load_model('auto_mpg.h5')
print(model.summary())

input_X_scaled = X_scaler.transform(input_X)

output_scaled = model.predict(input_X_scaled)

output = y_scaler.inverse_transform(output_scaled)

print(input_X)
print(output)