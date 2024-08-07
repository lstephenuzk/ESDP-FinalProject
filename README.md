# ESDP-FinalProject

This repository processes IAGOS (www.iagos.org) flight data (air temperature and relative humidity) from 1996 to 2022. NETCDF file for each month are combined into a single file, then preprocessing and quantile regression analysis is performed on the data in this file.

## src
  CombineData.ipynb - Combines monthly IAGOS NETCDF files from 1996 to 2022, selects columns of interests and saves dataframe as a python pickle file.

  Data_Processing.ipynb - Imports pickle file and performs data preprocessing and analysis. Variable of interest is selected by user then normalized to a constant pressure level. Data is then ordered into a time series and quantile regression is performed for the 5th, 50th, and 95th quantiles. 

## testing 
  test_value_range.py - Tests to check that latitude, longitude, air pressure, and relative humidity values are in the desired range.

  RunTests.ipynb - Runs tests in test_value_range.py file using pytest.

## Plots
  Plots output from Data_Processing.ipynb file: air temperature vs. air pressure scatter plot, normalized air temperature vs. air pressure scatter plot, normalized air temperature time series, and air temperature anomalies quantile regession results. 
