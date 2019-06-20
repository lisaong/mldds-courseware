import numpy as np
import pandas as pd
import pickle
import os
import boto3

class AutoMpg_Sklearn:
    def __init__(self, model_path):
        """Loads the model files"""
        self.X_scaler = pickle.load(open(os.path.join(model_path, 'X_scaler.pickle'), 'rb'))
        self.y_scaler = pickle.load(open(os.path.join(model_path, 'y_scaler.pickle'), 'rb'))
        self.model = pickle.load(open(os.path.join(model_path, 'model.pickle'), 'rb'))

    def preprocess(self, X):
        """Scales the raw input data"""
        return self.X_scaler.transform(X)

    def postprocess(self, yhat):
        """Unscales the raw predictions"""
        return self.y_scaler.inverse_transform(yhat)

    def predict(self, X):
        """Gets a prediction using the raw input data"""
        input_X_scaled = self.preprocess(X)
        yhat = self.model.predict(input_X_scaled)
        return self.postprocess(yhat)

def get_model_files():
    dest_path = os.getenv('MODEL_PATH', None)
    if dest_path is not None:
        s3 = boto3.resource('s3')
        dest_path = '/tmp'
        s3.download_file('zappa-8u6bzdej6', 'X_scaler.pickle', 
            f'{dest_path}/X_scaler.pickle')
        s3.download_file('zappa-8u6bzdej6', 'y_scaler.pickle',
            f'{dest_path}/y_scaler.pickle')
        s3.download_file('zappa-8u6bzdej6', 'model.pickle',
            f'{dest_path}/model.pickle')
    else:
        dest_path = '..' # try a local relative path
    return dest_path

if __name__ == '__main__':
    # for testing purposes
    m = AutoMpg_Sklearn('..')

    df = pd.read_csv('../auto-mpg.data-nans.txt',
                    delim_whitespace=True, # the data uses whitespaces as separators instead of commas
                    na_values=['?', 'NA'],  # to handle '?' in the horsepower column
                    names=['mpg', 'cylinders', 'displacement', 'horsepower', # data has no column names
                            'weight', 'acceleration', 'model_year', 'origin', 'car_name'])

    print(m.predict(df.loc[:, 'cylinders':'origin']))



