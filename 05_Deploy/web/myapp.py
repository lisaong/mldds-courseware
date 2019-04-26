from flask import Flask, render_template, request
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

@app.route('/form', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        X = [int(request.form.get('cylinders')),
            float(request.form.get('displacement')),
            float(request.form.get('horsepower')),
            float(request.form.get('weight')),
            float(request.form.get('acceleration')),
            int(request.form.get('model_year')),
            int(request.form.get('origin'))]

        prediction = model.predict([X]).ravel()[0]

        return f"""Prediction for {dict(request.form)}:<br>
             {prediction:.3f} mpg"""

    # render a jinja template using pre-defined parameters
    return render_template('form.html',
        model_year_min=70, model_year_max=82,
        cylinder_options=[4, 6, 8],
        origin_options=[1, 2, 3])

if __name__ == '__main__':
    app.run(debug=True, port=5000) # run app in debug mode on port 5000
