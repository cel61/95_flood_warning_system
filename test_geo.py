"Unit test for the geo module"

from floodsystem.geo import sort_station_distance, stations_within_radius, rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def  test_ssd():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    ssdtest = sort_station_distance(stations, p)
    assert(ssdtest[:1]) == [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995)]
    assert(ssdtest[-1:]) == [('Penberth', 467.53431870130544)]

def test_swr():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    swrtest = stations_within_radius(stations, p, 1)
    assert(swrtest(stations, p, 1)) == ["Cambridge Jesus Lock"]

def rbsn():

def rws():

def sbr():