from .utils import sorted_by_key
from .station import MonitoringStation
from . import datafetcher
from floodsystem.stationdata import build_station_list

def stations_level_over_threshold(stations, tol):
    dangerstations = []
    stations = build_station_list()
    for station in stations:
        rel_level= station.relative_water_level()
        if rel_level is not None:
            if rel_level > tol:
                data = (station.name,station.relative_water_level())
                dangerstations.append(data)
    final = sorted_by_key(dangerstations,1,reverse=True)
    return final
    

def stations_highest_rel_level(stations, N):
    result = []
    stations = build_station_list()
    highstations = stations_level_over_threshold(stations, 0)
    result = highstations[:N]
    return result