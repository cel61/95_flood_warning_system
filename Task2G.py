from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.datafetcher import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def run():
    stations = build_station_list()
    update_water_levels(stations)
    severe = stations_level_over_threshold(stations,1.5)
    high_old = stations_level_over_threshold(stations,1.2)
    moderate_old = stations_level_over_threshold(stations,1)
    low_old = stations_level_over_threshold(stations,0.7)
    high = high_old[len(severe):]
    moderate = moderate_old[len(high)+len(severe):]
    low = low_old[len(moderate)+len(high)+len(severe):]
    print("SEVERE RISK")
    print("\n")
    for a in severe:
        print("STATION NAME: ",a[0].name," RELATIVE LEVEL: ",a[1])
    print("\n")
    print("HIGH RISK")
    print("\n")
    for b in high:
        print("STATION NAME: ",b[0].name," RELATIVE LEVEL: ",b[1])
    print("\n")
    print("MODERATE RISK")
    print("\n")
    for c in moderate:
        print("STATION NAME: ",c[0].name," RELATIVE LEVEL: ",c[1])
    print("\n")
    print("LOW RISK")
    print("\n")
    for d in low:
        print("STATION NAME: ",d[0].name," RELATIVE LEVEL: ",d[1])
    print("\n")

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()