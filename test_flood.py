from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
from logging import raiseExceptions
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    s = stations_level_over_threshold(stations, 1)
    for i in s:
        assert i[1] > 1

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N=10
    s = stations_highest_rel_level(stations,N)
    assert len(s)==N