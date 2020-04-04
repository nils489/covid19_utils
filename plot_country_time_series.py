#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import pandas as pd

import data_preprocessing as dp

# parse arguments
parser = argparse.ArgumentParser(
    description='Plot COVID-19 data for a country.')
parser.add_argument('country',
                    type=str,
                    help='Name of country/region to plot data of')
parser.add_argument('--log',
                    action='store_true',
                    help='Plot with logarithmic y-axis.')
plot_group = parser.add_mutually_exclusive_group()
plot_group.add_argument('--new',
                    action='store_true',
                    help='Plot only new cases.')
plot_group.add_argument('--factor',
                    action='store_true',
                    help='Plot new cases v accumulated cases.')
args = parser.parse_args()

# build dataframe
ts = dp.load_time_series_data()
ts_line = dp.get_country_time_series_line(args.country, ts)

try:
    np_line = ts_line.values[0]
except IndexError:
    print("The specified country '" + args.country + "' was not found!")
    quit()

# build dataframes for plotting
ts_df = pd.DataFrame({'confirmed cases': np_line,
                      'dates': ts_line.columns})
ts_new_array = dp.get_new_cases(np_line)
ts_new_df = pd.DataFrame({'new cases': ts_new_array,
                          'dates': ts_line.columns})
if args.new:
    lineplot = ts_new_df.plot.line(x='dates', y='new cases', logy=args.log)
else:
    lineplot = ts_df.plot.line(x='dates', y='confirmed cases', logy=args.log)
plt.show()
