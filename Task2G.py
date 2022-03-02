from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.datafetcher import *
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation

def run():
    stations = build_station_list()
    update_water_levels(stations)
    severe_old = stations_level_over_threshold(stations,1.5)
    high_old = stations_level_over_threshold(stations,1.2)
    moderate_old = stations_level_over_threshold(stations,0.9)
    low_old = stations_level_over_threshold(stations,0.6)
    hs = high_old[len(severe_old):]
    ms = moderate_old[len(high_old):]
    ls = low_old[len(moderate_old):]
    severe_towns = []
    severe = []
    high_towns = []
    high = []
    low_town = []
    low = []
    moderate_town = []
    moderate = []
    for i in severe_old:
        if i[0].town == None:
            pass
        elif i[0].town in severe_towns:
            pass
        else:
            severe.append(i[0].town)
    for j in hs:
        if j[0].town == None:
            pass
        elif j[0].town in severe_towns or high_towns:
            pass
        else:
            high.append(j[0].town)
    for k in ms:
        if k[0].town == None:
            pass
        elif k[0].town in severe_towns or high_towns or moderate_town:
            pass
        else:
            moderate.append(k[0].town)
    for l in ls:
        if l[0].town == None:
            pass
        elif l[0].town in severe_towns or high_towns or moderate_town or low_town:
            pass
        else:
            low.append(l[0].town)
    severe.sort()
    high.sort()
    moderate.sort()
    low.sort()
    print("SEVERE RISK")
    print("\n")
    for a in severe:
        if a != None:
            print("TOWN NAME: ",a)
    print("\n")
    print("HIGH RISK")
    print("\n")
    for b in high:
        if b != None:
            print("TOWN NAME: ",b)
    print("\n")
    print("MODERATE RISK")
    print("\n")
    for c in moderate:
        if c != None:
            print("TOWN NAME: ",c)
    print("\n")
    print("LOW RISK")
    print("\n")
    for d in low:
        if d != None:
            print("TOWN NAME: ",d)
    print("\n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()