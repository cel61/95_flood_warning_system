from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
for i in stations:
    print(i.name,i.relative_water_level())