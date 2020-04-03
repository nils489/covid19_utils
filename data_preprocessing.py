import os
import pandas as pd


def load_time_series_data():
    # find the time_series csv file
    ts_path = './COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
    ts_filename = 'time_series_covid19_confirmed_global.csv'
    ts_filepath = os.path.join(ts_path, ts_filename)
    return pd.read_csv(ts_filepath)


def get_country_time_series_line(country, time_series_data_frame):
    ts = time_series_data_frame
    country_line = ts[(ts['Country/Region'] == country)]
    return country_line.drop(['Province/State',
                              'Country/Region',
                              'Lat', 'Long'], axis=1)
