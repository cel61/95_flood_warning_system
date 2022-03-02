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
    num_dates = matplotlib.dates.date2num(dates)
    if dates == [] or levels == []:
        x = []
        y = []
        date_range = np.linspace(0, 2, 60)
        for i in range(0,len(date_range)):
            x.append(station.typical_range[0])
            y.append(station.typical_range[1])
        plt.plot(date_range,x,color="green",label="Low Typical Range")
        plt.plot(date_range,y,color="blue",label="High Typical Range")
        plt.xlabel("numbered dates")
        plt.ylabel("water levels")
        plt.legend()
        plt.title(station.name, "(No valid data over selected time period)")
        plt.show()
    else:
        coefficent = np.polyfit(num_dates - num_dates[0], levels, p)
        p_new = np.poly1d(coefficent)
        date_range = np.linspace(num_dates[0], num_dates[-1], 60)
        x = []
        y = []
        for i in range(0,len(date_range)):
            x.append(station.typical_range[0])
            y.append(station.typical_range[1])
        plt.plot(date_range,x,color="green",label="Low Typical Range")
        plt.plot(date_range,y,color="blue",label="High Typical Range")
        plt.plot(num_dates, levels,color="red",label="Actual Levels")
        plt.plot(date_range, p_new(date_range - num_dates[0]), color="orange",label="Best fit line")
        plt.xlabel("numbered dates")
        plt.ylabel("water levels")
        plt.legend()
        plt.title(station.name)
        plt.show()