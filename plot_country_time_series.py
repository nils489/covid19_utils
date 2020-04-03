#!/usr/bin/env python

import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# parse arguments
parser = argparse.ArgumentParser(
    description='Plot COVID-19 data for a country.')
parser.add_argument('country',
                    type=str,
                    help='Name of country/region to plot data of')
parser.add_argument('--log',
                    type=bool,
                    default=False,
                    help='Flag to determine whether or not to '
                    'plot logarithmic.')
parser.add_argument('--new',
                    type=bool,
                    default=False,
                    help='If True, plot only new cases. '
                    'default: False')
args = parser.parse_args()
cr_key = args.country

# find the time_series csv file
ts_path = './COVID-19/csse_covid_19_data/csse_covid_19_time_series/'
ts_filename = 'time_series_covid19_confirmed_global.csv'
ts_filepath = os.path.join(ts_path, ts_filename)

# build dataframe
ts = pd.read_csv(ts_filepath)
line_country = ts[(ts['Country/Region'] == cr_key)]
ts_country = line_country.drop(['Province/State',
                                'Country/Region',
                                'Lat', 'Long'], axis=1)

try:
    np_line = ts_country.values[0]
except IndexError:
    print("The specified country '" + cr_key + "' was not found!")
    quit()

# build dataframes for plotting
ts_df = pd.DataFrame({'confirmed cases': np_line,
                      'dates': ts_country.columns})
# dataframe with new cases
ts_new_list = [0]
for ind in range(1, np_line.shape[0]):
    ts_new_list.append(np_line[ind] - np_line[ind-1])
ts_new_array = np.array(ts_new_list)
ts_new_df = pd.DataFrame({'new cases': ts_new_array,
                          'dates': ts_country.columns})
if args.new:
    lineplot = ts_new_df.plot.line(x='dates', y='new cases', logy=args.log)
else:
    lineplot = ts_df.plot.line(x='dates', y='confirmed cases', logy=args.log)
plt.show()
