from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    dt = 10
    needed_stations = stations_highest_rel_level(stations,5)
    print(needed_stations)
    for station in stations:
        for i in needed_stations:
            if i[0]==station.name:
                dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
                plot_water_levels(station,dates,levels)
        

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()