#!/usr/bin/env python

import os
import sys
import argparse
import matplotlib.pyplot as plt
import pandas as pd

# parse arguments
parser = argparse.ArgumentParser(description='Plot COVID-19 data for a country.')
parser.add_argument('country',
                    type=str,
                    help='Name of country/region to plot data of')
parser.add_argument('--log',
                    type=bool,
                    default=False,
                    help='Flag to determine whether or not to plot logarithmic.')
args = parser.parse_args()

cr_key = args.country
ts_path = './COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
ts_filename = 'time_series_covid19_confirmed_global.csv'
ts_filepath = os.path.join(ts_path, ts_filename)

ts = pd.read_csv(ts_filepath)
line_country = ts[ (ts['Country/Region'] == cr_key) ]
ts_country = line_country.drop(['Province/State',
                                'Country/Region',
                                'Lat', 'Long'], axis=1)
np_ts_country = ts_country.values
try:
    ts_df = pd.DataFrame({'confirmed cases': ts_country.values[0],
                          'dates': ts_country.columns})
    lineplot = ts_df.plot.line(x='dates', y='confirmed cases', logy=args.log)
    plt.show()
    pass
except IndexError as e:
    print("The specified country '" +cr_key+ "' was not found!")
