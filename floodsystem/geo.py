# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
#This module contains a collection of functions related to
#geographical data.

#"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from .station import MonitoringStation
from . import datafetcher
from floodsystem.stationdata import build_station_list


def sort_station_distance(stations, p):
    names =[]
    distlst =[]
    stations = build_station_list()
    for station in stations:
        names.append(station.name)
        distlst.append(haversine (station.coord, p))
       
    
    stationdistance = list(zip(names, distlst))
    stationdistance = sorted_by_key(stationdistance, 1)
    return stationdistance

