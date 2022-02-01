from floodsystem.geo import sort_station_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)

    numberofstations = sort_station_distance(stations, p)
    print(numberofstations[:10])
    print(numberofstations[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()



