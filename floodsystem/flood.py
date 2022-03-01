from .utils import sorted_by_key
from .station import MonitoringStation
from . import datafetcher
from floodsystem.stationdata import build_station_list, update_water_levels

def stations_level_over_threshold(stations, tol):
    s = []
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level != None and rel_level > tol:
            l = (station, rel_level)
            s.append(l)
            result = sorted_by_key(s,1,reverse=True)
    return result
    

def stations_highest_rel_level(stations, N):
    result = []
    stations = build_station_list()
    highstations = stations_level_over_threshold(stations, 0)
    result = highstations[:N]
    return result