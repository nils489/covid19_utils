#!/usr/bin/env python

import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

if len(sys.argv) != 2:
    print("You need to provide the name of the country " \
          "you want to plot data for!")
    print("Usage: plot_country_time_series.py" \
          "<Name of Country/Region>")
    raise ValueError("Wrong number of arguments.")

cr_key = str(sys.argv[1])

ts_path = './COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
ts_filename = 'time_series_covid19_confirmed_global.csv'
ts_filepath = os.path.join(ts_path, ts_filename)

ts = pd.read_csv(ts_filepath)
line_germany = ts[ (ts['Country/Region'] == cr_key) ]
ts_germany = line_germany.drop(['Province/State',
                                'Country/Region',
                                'Lat', 'Long'], axis=1)
np_ts_germany = ts_germany.values
try:
    plt.plot(np_ts_germany[0])
    plt.show()
except IndexError as e:
    print(e)
