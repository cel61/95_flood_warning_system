# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
#This module contains a collection of functions related to
#geographical data.

#"""
from gettext import install
from numpy import sort
from haversine import haversine, Unit
from pyparsing import Or
from sqlalchemy import true


from .utils import sorted_by_key
from .station import MonitoringStation
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

def rivers_by_station_number(stations, N):
    stations = build_station_list()
    rstations = []
    for station in stations:
        if station.river != None:
            rstations.append(station.river)
        rstations.sort()
    def count(list):
        count_dict = {}
        for station in list:
            count_dict[station] = list.count(station)
        return dict(sorted(count_dict.items(), key=lambda x:x[1]))
    numstations = count(rstations)
    result = list(numstations.items())
    final =  result[(-1*N):]
    return final

def typical_range_consistent(self):
    if self.typical_range == None:
        return False
    elif self.typical_range[0] > self.typical_range[1]:
        return False
    else:
        return True

def inconsistent_typical_range_stations(stations):
    inconsistent_stations = []
    for i in stations:
        if typical_range_consistent(i) == False:
            inconsistent_stations.append(i.name)
    inconsistent_stations.sort()
    return inconsistent_stations
