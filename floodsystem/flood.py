from .utils import sorted_by_key
from .station import MonitoringStation
from . import datafetcher
from floodsystem.stationdata import build_station_list

def stations_level_over_threshold(stations, tol):
    dangerstations = []
    stations = build_station_list()
    for station in stations:
        if station.relative_water_level > tol:
            data = (station.name,station.relative_water_level)
            dangerstations.append(data)
    final = sorted_by_key(dangerstations,1,reverse=True)
    return final