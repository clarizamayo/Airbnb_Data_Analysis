import pandas as pd
import numpy as np
import requests
import datetime
import kaggle

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
            # push to database
            # load data from database into pandas
            # do basic analysis
    
        yield stroke # return dataframe

if __name__ == '__main__':
    main()
