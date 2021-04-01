"""
    Priorities:
        1. Get the functionality to work
        2. Get the code well organized 
        (though it is easy to get functionality to work if your code is well organized)
        3. Make it efficient
"""
import pandas as pd
from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy 
from get_data import get_stroke_data
from get_data import creating_db
from get_data import check_db

app = Flask(__name__)
app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q7zeec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stroke_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 



data1= next(check_db("airbnb2017"))
data2= next(check_db("updated_airbnb2017"))

@app.route('/', methods=("POST", "GET"))
def homepage():
    return render_template('base.html')

@app.route('/airbnb2017', methods=("POST", "GET"))
def html_table():
    return render_template('table_1.html', data=[row for index,row in data1.iterrows()])

@app.route('/updated_airbnb2017', methods=("POST", "GET"))
def html_2_table():
    return render_template('table_2.html', data=[row for index,row in data2.iterrows()])

@app.route('/airbnb2017/api', methods=("POST", "GET"))
def original_api():
    return data1.to_json(orient="split")

@app.route('/updated_airbnb2017/api', methods=("POST", "GET"))
def updated_api():
    return data2.to_json(orient="split")

@app.route('/airbnb2017/api/<num>', methods=("POST", "GET"))
def original_api_row(num):
    return data1.iloc[int(num)].to_json(orient="split")

@app.route('/updated_airbnb2017/api/<num>', methods=("POST", "GET"))
def updated_api_row(num):
    return data2.iloc[int(num)].to_json(orient="split")

@app.route('/airbnb2017/api/column/<name>', methods=("POST", "GET"))
def original_api_column(name):
    return data1[name].to_json(orient="split")

@app.route('/updated_airbnb2017/api/column/<name>', methods=("POST", "GET"))
def updated_api_column(name):
    return data2[name].to_json(orient="split")

if __name__ == '__main__':
    app.run(debug=True)