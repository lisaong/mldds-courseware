from flask import Flask
import pandas as pd

from models import AutoMpg_Sklearn

app = Flask(__name__)
model = AutoMpg_Sklearn()

@app.route('/')
def hello():
    df = pd.read_csv('../auto-mpg.data-nans.txt',
                    delim_whitespace=True, # the data uses whitespaces as separators instead of commas
                    na_values=['?', 'NA'],  # to handle '?' in the horsepower column
                    names=['mpg', 'cylinders', 'displacement', 'horsepower', # data has no column names
                            'weight', 'acceleration', 'model_year', 'origin', 'car_name'])

    return repr(model.predict(df.loc[:, 'cylinders':'origin']))

if __name__ == '__main__':
    app.run(debug=True, port=5000) # run app in debug mode on port 5000
