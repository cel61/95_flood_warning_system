from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    stationlist = stations_within_radius(stations, p, 10)
    alphab = sorted(stationlist)
    print(alphab)




if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()