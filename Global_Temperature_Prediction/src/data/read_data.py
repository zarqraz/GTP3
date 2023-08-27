import pandas as pd
import json
###
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM


def read_data() -> pd.DataFrame:
    
    temperature2 = pd.read_csv("data/temperature.csv")
    temperature2 = temperature2[temperature2.columns[2:4]]
    temperature2.rename(columns = {'Global average temperature anomaly relative to 1961-1990':'Anomaly'}, inplace = True)
    temperature2
    temperature = temperature2.values
    temperature

    temperature2 = temperature2.set_index(temperature2['Year'])
    temperature2 = temperature2.drop('Year', axis=1)
    temperature2.index.name = None
    temperature2

    co2e = pd.read_excel("data/co2emission.xlsx", index_col=0)
    co2e.rename(columns = {'CO2 GtC/yr':'Emission'}, inplace = True)
    # emissions = co2e.Emission.values
    # emissions

    co2e.index.name = None
    co2e

    co2ppm = pd.read_excel("data/co2ppm.xlsx")
    co2ppm.rename(columns = {'CO2EQ ppm':'Concentration'}, inplace = True)
    co2ppm
    # concentration = co2ppm["Concentration"].values
    # concentration

    dane = co2ppm
    dane = dane.set_index(co2ppm['Unnamed: 0'])
    dane = dane.drop('Unnamed: 0', axis=1)
    dane.index.name = None
    dane["Emissions"] = co2e["Emission"]
    dane["Anomaly"] = temperature2["Anomaly"]
    dane
    # import matplotlib.pyplot as plt

    # dane_stand = dane
    # dane_stand
    # dane_stand['Anomaly'] = (dane_stand['Anomaly'] - dane_stand['Anomaly'].mean()) / dane_stand['Anomaly'].std()
    # dane_stand['Concentration'] = (dane_stand['Concentration'] - dane_stand['Concentration'].mean()) / dane_stand['Concentration'].std()
    # dane_stand['Emissions'] = (dane_stand['Emissions'] - dane_stand['Emissions'].mean()) / dane_stand['Emissions'].std()
    # dane_stand
    # print(dane_stand)

    # fig, ax = plt.subplots()
    # ax.plot(dane.index, dane["Anomaly"])
    # ax.plot(dane.index, dane["Concentration"])
    # ax.plot(dane.index, dane["Emissions"])
    # plt.show()
    dane = dane.truncate(after=2022)
    






    return dane