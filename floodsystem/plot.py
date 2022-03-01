from cProfile import label
from turtle import color
import matplotlib
import matplotlib.pyplot as plt
from .station import MonitoringStation
from . import datafetcher
from datetime import datetime, timedelta
from .stationdata import build_station_list, update_water_levels
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    plt.xlabel("dates")
    plt.ylabel("water levels")
    plt.xticks(rotation=45)
    plt.title(station.name)
 
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    datafetcher.fetch_latest_water_level_data(station)
    update_water_levels(station)
    num_dates = matplotlib.dates.date2num(dates)
    coefficent= np.polyfit(num_dates - num_dates[0], levels, p)
    p_new = np.poly1d(coefficent)
    x = polyfit(dates,levels,p_new)
    plt.plot(num_dates, levels,color="red",label="Actual Levels")
    plt.plot(num_dates-x[1], levels, color="orange",label="Best fit line")
    plt.xlabel("numbered dates")
    plt.ylabel("water levels")
    plt.title(station.name)
    plt.show()



