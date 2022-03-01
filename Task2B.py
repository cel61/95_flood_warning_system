from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
<<<<<<< HEAD
    result = stations_level_over_threshold(stations, 0)
=======
    tol = 0.8
    result = stations_level_over_threshold(stations, tol)
    print(result)
>>>>>>> dbeac4c83aae5e204a419be0d75167617e74ca1b
    for i in result:
        print(i)



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()