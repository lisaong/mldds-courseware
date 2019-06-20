from flask import Flask, render_template, request
import pandas as pd
import os

from models import AutoMpg_Sklearn, get_model_files

app = Flask(__name__)
model_path = get_model_files()
model = AutoMpg_Sklearn(model_path=model_path)

@app.route('/', methods=['GET', 'POST'])
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
        return render_template('prediction.html', parameters=dict(request.form),
            prediction=prediction)

    else:
        return render_template('form.html',
            model_year_min=70, model_year_max=82,
            cylinder_options=[4, 6, 8],
            origin_options=[1, 2, 3])

if __name__ == '__main__':
    app.run(debug=True, port=5000) # run app in debug mode on port 5000
