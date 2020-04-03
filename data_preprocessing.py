import os
import numpy as np
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


def get_new_cases(time_series_array):
    # dataframe with new cases
    ts_new_list = [0]
    for ind in range(1, time_series_array.shape[0]):
        ts_new_list.append(time_series_array[ind] - time_series_array[ind-1])
    return np.array(ts_new_list)
