"""
    Priorities:
        1. Get the functionality to work
        2. Get the code well organized 
        (though it is easy to get functionality to work if your code is well organized)
        3. Make it efficient
"""
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
db = SQLAlchemy(app)
  
s = get_stroke_data()
db = creating_db()

@app.route('/', methods=("POST", "GET"))
def homepage():
    return f"This route is working"


# @app.route('/', methods=("POST", "GET"))
# def html_table():
#     stroke = next(s)
#     return render_template('simple.html',  tables=[stroke.to_html(classes='data')], titles=stroke.columns.values)

# def test_get_gender():
#     test_case = """
#     {"id":{"0":9046,"2":31112,"5":56669,"6":53882,"13":8213,"16":56112,"17":34120,"19":25226,"23":64778,"24":4219},"gender":{"0":"Male","2":"Male","5":"Male","6":"Male","13":"Male","16":"Male","17":"Male","19":"Male","23":"Male","24":"Male"},"age":{"0":67.0,"2":80.0,"5":81.0,"6":74.0,"13":78.0,"16":64.0,"17":75.0,"19":57.0,"23":82.0,"24":71.0},"hypertension":{"0":0,"2":0,"5":0,"6":1,"13":0,"16":0,"17":1,"19":0,"23":0,"24":0},"heart_disease":{"0":1,"2":1,"5":0,"6":1,"13":1,"16":1,"17":0,"19":1,"23":1,"24":0},"ever_married":{"0":"Yes","2":"Yes","5":"Yes","6":"Yes","13":"Yes","16":"Yes","17":"Yes","19":"No","23":"Yes","24":"Yes"},"work_type":{"0":"Private","2":"Private","5":"Private","6":"Private","13":"Private","16":"Private","17":"Private","19":"Govt_job","23":"Private","24":"Private"},"Residence_type":{"0":"Urban","2":"Rural","5":"Urban","6":"Rural","13":"Urban","16":"Urban","17":"Urban","19":"Urban","23":"Rural","24":"Urban"},"avg_glucose_level":{"0":228.69,"2":105.92,"5":186.21,"6":70.09,"13":219.84,"16":191.61,"17":221.29,"19":217.08,"23":208.3,"24":102.87},"bmi":{"0":36.6,"2":32.5,"5":29.0,"6":27.4,"13":null,"16":37.5,"17":25.8,"19":null,"23":32.5,"24":27.2},"smoking_status":{"0":"formerly smoked","2":"never smoked","5":"formerly smoked","6":"never smoked","13":"Unknown","16":"smokes","17":"smokes","19":"Unknown","23":"Unknown","24":"formerly smoked"},"stroke":{"0":1,"2":1,"5":1,"6":1,"13":1,"16":1,"17":1,"19":1,"23":1,"24":1}}
#     """

#     test_data = pd.read_csv("healthcare-dataset-stroke-data.csv")
#     return_data = get_gender("Male", test_data)
#     assert return_data[:10].to_json() == test_case.strip()

# def get_gender(gender, stroke):
#     # other processing goes here
#     if gender not in ["Male", "Female"]:
#         raise Exception("Expected Male or Female")
#     return stroke[stroke["gender"] == gender]

# @app.route('/api/gender/<gender>')
# def get_gender_api(gender):
#     try:
#         stroke = next(s)
#         return get_gender(gender, stroke).to_json()
#     except Exception as e:
#         return str(e), 400

# @app.route('/gender/<gender>')
# def get_gender_table(gender):
#     try:
#         stroke = next(s)
#         return get_gender(gender, stroke).to_html()
#     except Exception as e:
#         return str(e), 400

# @app.route('/test/gender')
# def test_gender_route():
#     try:
#         test_get_gender()
#         return "Success", 200
#     except:
#         return "Failed", 400

"""
    Each function should have a single responsibility/perform a single sort of action
    1. Fetching/getting something (e.g. download data)
    2. Parsing or transforming something (e.g. perform analysis on data like linear regression)
    3. Printing out or converting something (e.g. convert to table, html, json, etc.)
"""

"""
    When thinking about how to structure functions and classes here's my principles:
    * GUIDING PRINCIPLE: If it makes the code simpler and easier to follow: DO IT"
    1. All related data should be part of the class (e.g. stroke data is all in one class)
    2. I want to provide clear interfaces for the other parts of my application
       to interact with. (i.e. I don't want to allow direct access to the dataframe)
"""

"""
    Unit testing is just testing the correctness of a function based on known
    inputs and outputs.
"""
if __name__ == '__main__':
    app.run(debug=True)