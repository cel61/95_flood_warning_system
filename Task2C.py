from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    N = 10
    stations = build_station_list()
    r = stations_highest_rel_level(stations,N)
    for i in r:
        print(i[0], i[1])


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()