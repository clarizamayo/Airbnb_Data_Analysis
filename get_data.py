import pandas as pd
import numpy as np
import datetime
import kaggle

from sqlalchemy import create_engine
engine = create_engine('sqlite:///project_2.db', echo=False)

links = ["fedesoriano/stroke-prediction-dataset","dgomonov/new-york-city-airbnb-open-data","ivanovskia1/nyc-airbnb-rental-data-october-2017"]
def get_stroke_data(): # Split this into get_stroke_data and parse_stroke_data
    api = kaggle.KaggleApi()
    api.authenticate()
    for link in links:
        api.dataset_download_files(link, unzip=True, quiet=False)
    stroke = pd.read_csv("healthcare-dataset-stroke-data.csv")
    open_nyc_data = pd.read_csv("AB_NYC_2019.csv")
    airbnb_2017 = pd.read_csv("New York.csv")
    
    start = datetime.datetime.now()
    while True:
        if datetime.datetime.now() > (start +  datetime.timedelta(days=1)):
            api.authenticate()
            for link in links:
                api.dataset_download_files(link, unzip=True, quiet=False)
            stroke = pd.read_csv("healthcare-dataset-stroke-data.csv")
            open_nyc_data = pd.read_csv("AB_NYC_2019.csv")
            airbnb_2017 = pd.read_csv("New York.csv")
        yield stroke
        yield open_nyc_data
        yield airbnb_2017 

def creating_db():  
    dataframes = get_stroke_data()
    stroke = next(dataframes)
    open_nyc = next(dataframes)
    airbnb2017 = next(dataframes)
    moving_stroke_to_db = stroke.to_sql('stroke', con=engine, if_exists='append')
    moving_opennyc_to_db = open_nyc.to_sql('opennyc', con=engine, if_exists='append')
    moving_airbnb2017_to_db = airbnb2017.to_sql('airbnb2017', con=engine, if_exists='append')

def check_db(table_name):
    df= pd.read_sql_table(table_name, con=engine)
    while True:
        yield df

if (__name__ == "__main__"):
     creating_db()
     check_db(table_name="airbnb2017")