from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    tol = 0.8
    result = stations_level_over_threshold(stations, tol)
    for i in result:
        print(i[0], i[1])



if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()