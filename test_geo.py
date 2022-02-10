"Unit test for the geo module"

from ast import Break
from random import randint
from turtle import st
from floodsystem.geo import sort_station_distance, stations_within_radius, inconsistent_typical_range_stations, rivers_by_station_number, rivers_with_station, stations_by_river, typical_range_consistent
from floodsystem.stationdata import build_station_list
from logging import raiseExceptions
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

stations = build_station_list()

"""testing given 0 coordinates return 0 distance them and the distance between two example coordinates is accurate"""
def  test_sort_station_distance():
    test_distance = sort_station_distance([MonitoringStation(0, 0, "hello", (22,22), 0, 0, 0)], (0,0))
    for i in test_distance:
        if i[0] == "hello":
            assert test_distance[0][1] == 0
            assert round(test_distance[0][1] ,2) == 3416

"""testing the output contains a given station, and that the output is sorted"""
def test_stations_within_radius():
    p = (52.2053, 0.1218)
    swrtest = stations_within_radius(stations, p, 1)
    assert(swrtest[0]) == "Cambridge Jesus Lock"
    stations_within_0 = stations_within_radius(stations,(52.2053, 0.1218),0)
    assert len(stations_within_0) == 0


"""testing rivers_by_station_number is properly sorted and returns the correct number of outputs"""
def Test_rivers_by_station_number():
    Testlist = rivers_by_station_number(MonitoringStation, 11)
    assert Testlist[10][1] == Testlist[-1][1]
    "Checking if last river same as Nth river (11)"


"""testing the correct output for consistent typical data ranges is returned using example stations"""
def test_typical_range_consistent():
    station1 = MonitoringStation(0, 0, 0, (0,0), (1.8, 0.3), 0, (0,0))
    station2 = MonitoringStation(0, 0, 0, (0,0), None, 0, (0,0))
    station3 = MonitoringStation(0, 0, 0, (0,0), (0, 0.5), 0, (0,0))
    assert typical_range_consistent(station1) == False
    assert typical_range_consistent(station2) == False
    assert typical_range_consistent(station3) == True

"""testing the function is properly sorted"""
def test_inconsistent_typical_range_stations():
    s = inconsistent_typical_range_stations(stations)
    s.sort()
    assert inconsistent_typical_range_stations(stations) == s
    """tests requirements of inconsistent_typical_range_stations"""
    stations = [
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, None, None, None),
        MonitoringStation(None, None, None, None, None, None, None)]
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    # checks the type of inconsistent_stations
    assert type(inconsistent_stations) == list
    # checks that the length of inconsistent stations is 2
    assert len(inconsistent_stations) == 2

"""testing the function properly returns the correct rivers that contain examples station (0) and that the list is sorted"""
def test_rivers_with_station():
    assert len(rivers_with_station(stations)) == 2164
    river_station = MonitoringStation(0, 0, 0, (0,0), (0, 0), "rws test", 0)
    rivers = rivers_with_station(river_station)
    for i in rivers:
        if i == "rws test":
            assert i == "rws test" 


"""testing that the function properly counts the number of (example) stations on different rivers"""
def test_stations_by_river():

    stationariv1 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "River Aire", 0)
    stationbriv3 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "River Aire", 0)
    stationcriv2 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "River Thames", 0)
    stationstest = [stationariv1,stationcriv2,stationbriv3]

    river_to_stations = stations_by_river(stationstest)

    assert len(river_to_stations["River Aire"]) == 24
    assert len(river_to_stations["River Thames"]) == 54