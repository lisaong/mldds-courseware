import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read data
df = pd.read_csv('auto-mpg.data.txt',
                 delim_whitespace=True, # the data uses whitespaces as separators instead of commas
                 na_values=['?'],  # to handle '?' in the horsepower column
                 names=['mpg', 'cylinders', 'displacement', 'horsepower', # data has no column names
                       'weight', 'acceleration', 'model_year', 'origin', 'car_name'])

df.dropna(inplace=True)

# This returns a view, so we can call it again without resulting in a copy of the data
X = df.loc[:, 'cylinders':'origin']
y = df.mpg

# A typical naming convention is to use upper case (e.g. X) for 2-d matrices, lower case (e.g. y) for 1-d vector
train_X, test_X, train_y, test_y = train_test_split(X, y, 
                                                    test_size=0.1, # reserve about 10% of the data for test
                                                    random_state=42) # set random state so we
                                                                     # get the same dataset each time
                                                                     # we run this code.
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

X_scaler = StandardScaler()
y_scaler = StandardScaler()

# 1. initialize the scaler
# 2. scale both X datasets
train_X_scaled = X_scaler.fit_transform(train_X)
test_X_scaled = X_scaler.transform(test_X)

# Repeat for y
# 1. initialize the scaler
y_scaler.fit(train_y.values.reshape(-1, 1))

# 2. scale both y series
train_y_scaled = y_scaler.transform(train_y.values.reshape(-1, 1))
test_y_scaled = y_scaler.transform(test_y.values.reshape(-1, 1))

lin = LinearRegression()
lin.fit(train_X_scaled, train_y_scaled)

pred_scaled = lin.predict(test_X_scaled)

print('MSE:', mean_squared_error(test_y_scaled, pred_scaled)) # lower is better
print('R2:', r2_score(test_y_scaled, pred_scaled)) # higher and close to 1 is better

# Save model and scalers so that we can load them upon deployment
# http://scikit-learn.org/stable/modules/model_persistence.html
import pickle
pickle.dump(X_scaler, open('X_scaler.sav', 'wb'))
pickle.dump(y_scaler, open('y_scaler.sav', 'wb'))
pickle.dump(lin, open('model.sav', 'wb'))
