from floodsystem.datafetcher import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt

def run():
    stations = build_station_list()
    update_water_levels(stations)
    s = stations_highest_rel_level(stations,5)
    dt = 2
    for i in s:
        dates,levels = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(i[0], dates, levels, 4)


    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()