import pytest
import pandas as pd

dataset = pd.read_pickle("/p/project1/deepacf/stephenson1/ESDP-FinalProject/iagos_combined.pkl")

def test_air_press():
    assert dataset['air_press'].min() >= 150
    assert dataset['air_press'].max() <= 400

def test_lat_lon():
    assert dataset['lat'].min() >= 0
    assert dataset['lat'].max() <= 68
    assert dataset['lon'].min() >= -80
    assert dataset['lon'].max() <= 0

def test_rhl():
    assert dataset['RHL'].min() >= 0
    assert dataset['RHL'].max() <= 1

def test_rhi():
    assert dataset['RHI'].min() >= 0
    assert dataset['RHI'].max() <= 1

def test_air_temp():
    assert dataset['air_temp'].min() >= 193
    assert dataset['air_temp'].max() <= 333






