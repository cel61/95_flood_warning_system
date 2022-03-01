from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    result = stations_level_over_threshold(stations, 0)
    for i in result:
        print(i)



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()