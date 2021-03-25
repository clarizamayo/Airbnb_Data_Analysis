import pandas as pd
import numpy as np
import requests
import datetime
import kaggle

from sqlalchemy import create_engine
engine = create_engine('sqlite:///stroke.db', echo=False)

def get_stroke_data(): # Split this into get_stroke_data and parse_stroke_data
    api = kaggle.KaggleApi()
    api.authenticate()
    api.dataset_download_files("fedesoriano/stroke-prediction-dataset", unzip=True, quiet=False)
    stroke = pd.read_csv("healthcare-dataset-stroke-data.csv")
    start = datetime.datetime.now()
    while True:
        if datetime.datetime.now() > (start +  datetime.timedelta(days=1)):
            api.authenticate()
            api.dataset_download_files("fedesoriano/stroke-prediction-dataset", unzip=True, quiet=False)
            stroke = pd.read_csv("healthcare-dataset-stroke-data.csv")
        yield stroke

def creating_db():  
    stroke_dataframe = get_stroke_data()
    moving_to_db = next(stroke_dataframe).to_sql('stroke', con=engine, if_exists='append')

def check_db():
    with engine.connect() as conn:
        rows = conn.execute("SELECT * FROM stroke;")
        for row in rows:
            print(row)


if (__name__ == "__main__"):
     creating_db()
     check_db()

#To autenticate kaggle
# export KAGGLE_USERNAME=clarizamayo
# export KAGGLE_KEY=35e52457b36e90c1f9cc6da6459859c7