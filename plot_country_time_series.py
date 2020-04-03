#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data_preprocessing import load_data

# parse arguments
parser = argparse.ArgumentParser(
    description='Plot COVID-19 data for a country.')
parser.add_argument('country',
                    type=str,
                    help='Name of country/region to plot data of')
parser.add_argument('--log',
                    action='store_true',
                    help='Plot with logarithmic y-axis.')
parser.add_argument('--new',
                    action='store_true',
                    default=False,
                    help='Plot only new cases.')
args = parser.parse_args()

# build dataframe
ts = load_data()
line_country = ts[(ts['Country/Region'] == args.country)]
ts_country = line_country.drop(['Province/State',
                                'Country/Region',
                                'Lat', 'Long'], axis=1)

try:
    np_line = ts_country.values[0]
except IndexError:
    print("The specified country '" + args.country + "' was not found!")
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
