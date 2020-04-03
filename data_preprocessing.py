import os
import pandas as pd


def load_data():
    # find the time_series csv file
    ts_path = './COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
    ts_filename = 'time_series_covid19_confirmed_global.csv'
    ts_filepath = os.path.join(ts_path, ts_filename)
    return pd.read_csv(ts_filepath)
