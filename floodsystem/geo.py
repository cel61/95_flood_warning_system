# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
#This module contains a collection of functions related to
#geographical data.

#"""
from gettext import install


from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine, Unit
from . import datafetcher
from floodsystem.stationdata import build_station_list


def sort_station_distance(stations, p):
    names =[]
    distlst =[]
    stations = build_station_list()
    for station in stations:
        names.append(station.name)
        distlst.append(haversine(station.coord, p))
       
    
    stationdistance = list(zip(names, distlst))
    stationdistance = sorted_by_key(stationdistance, 1)
    return stationdistance

def stations_within_radius(stations, centre, r):
    stations = build_station_list()
    names = []
    for station in stations:
        if (haversine(station.coord, centre)) < r:
            names.append(station.name)
    return names
    

def rivers_with_station(stations):
    stations = build_station_list()
    rivers = []
    for station in stations:
        if station.river != None:
            rivers.append(station.river)
    return rivers

def stations_by_river(stations):
    stations = build_station_list()
    aire = []
    cam = []
    thames = []
    for station in stations:
        if station.river == "River Aire":
            aire.append(station.name)
        if station.river == "River Cam":
            cam.append(station.name)
        if station.river == "River Thames":
            thames.append(station.name)
    aire.sort()
    cam.sort()
    thames.sort()
    resultlist = [aire, cam, thames]
    return resultlist
