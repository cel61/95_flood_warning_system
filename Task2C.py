from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    N = 10
    stations = build_station_list()

    # finding N (10) stations with highest water levels

    r = stations_highest_rel_level(stations,N)
    for i in r:
        #printing the name and level for these ten stations
        print(i[0].name, i[1])



if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()