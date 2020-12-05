from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask import render_template, jsonify,request
import requests

app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q7zeec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clariza_mayo_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app) 


class Emissions(db.Model):
    __tablename__ = "World CO2 Emissions"
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(255), nullable=True) 
    emission_1990 = db.Column(db.Float, nullable=True)
    emission_2005 = db.Column(db.Float, nullable=True)
    emission_2017 = db.Column(db.Float, nullable=True)
    perc_world_emissions = db.Column(db.Integer, nullable=True)
    perc_change_2017_2019 = db.Column(db.Integer, nullable=True)
    per_land_area = db.Column(db.Integer, nullable=True)
    per_capita = db.Column(db.Integer, nullable=True)
    
class Population(db.Model):
    __tablename__ = "World Population in 2005"
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(255), nullable=True) 
    population = db.Column(db.Integer, nullable=True)


# set up your index view to show your "home" page
# it should include:
# links to any pages you have
# information about your data
# information about how to access your data
# you can choose to output data on this page
@app.route('/', methods=['GET'])
def index():
    data = Emissions.query.all()
    return render_template('index.html', data=data)

# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data

# change this to return your data
@app.route('/api', methods=['GET'])
def get_data():
    table = Emissions.query.all()
    d = {row.id:row.name for row in table}
    return jsonify(d)

# # change this to allow users to add/update data
@app.route('/api', methods=['POST'])
def add_data():
    if request.method == "POST":
        print(request.form)
        for k,v in request.args.items():
            print(k,v)
            # pass
        return jsonify({})
        
# # change this to allow the deletion of data
@app.route('/api', methods=['DELETE'])
def delete_data():
    for k,v in request.args.items():
        pass
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)