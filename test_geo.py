"Unit test for the geo module"

from ast import Break
from turtle import st
from floodsystem.geo import sort_station_distance, stations_within_radius, rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
from logging import raiseExceptions
from floodsystem.station import MonitoringStation

stations = build_station_list()

def  test_sort_station_distance():
    test_distance = sort_station_distance([MonitoringStation(0, 0, 0, (22,22), 0, 0, 0)], (0,0))
    assert test_distance[0][0] == 0
    assert round(test_distance[0][1] ,2) == 3416


def test_stations_within_radius():
    p = (52.2053, 0.1218)
    swrtest = stations_within_radius(stations, p, 1)
    assert(swrtest(stations, p, 1)) == ["Cambridge Jesus Lock"]
    if swrtest(stations, p, 1) != ["Cambridge Jesus Lock"]:
        raise Exception("Error: function could not be carried out")  
    stations_within_10k = stations_within_radius(stations,(52.2053, 0.1218),10)
    assert stations_within_10k == sorted(stations_within_10k)
    stations_within_0 = stations_within_radius(stations,(52.2053, 0.1218),0)
    assert len(stations_within_0) == 0

def test_rivers_by_stations_number():
    



def test_rivers_with_station():
    assert len(rivers_with_station(stations)) == 950
    assert rivers_with_station(stations) == rivers_with_station(stations).sort()
    river_station = MonitoringStation(0, 0, 0, (0,0), (0, 0), "rws test", 0)
    rivers = rivers_with_station([river_station])
    assert rivers[0] == "rws test" 

def test_stations_by_river():

    stationariv1 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "riv1", 0)
    stationbriv1 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "riv1", 0)
    stationcriv2 = MonitoringStation(0, 0, 0, (0,0), (0, 0), "riv2", 0)

    river_to_stations = stations_by_river([stationariv1, stationbriv1, stationcriv2])

    assert len(river_to_stations["riv1"]) == 2
    assert len(river_to_stations["riv2"]) == 1