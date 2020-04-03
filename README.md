# covid19_utils
covid19_utils is a collection of some utility scripts to visualize the spread of the COV-SARS2 virus and the connected desease COVID-19.

## Installation
Before running the covid19_utils, make sure, you have git installed.
Additionally you'll need the following python packages:

numpy

matplotlib

pandas

After the installation of the dependencies make sure, you're in the covid19_utils directory and run:
```
bash setup.sh
```
This will clone the CSSE COVID-19 repository to your working directory.

## Update
To update the CSSE data, you can either manually pull from the github repo or run the provided update script:
```
bash update.sh
```

## Plot data
To plot the data from a country of your choice, run
```
python plot_country_time_series.py <Name of Country/Region>
```
