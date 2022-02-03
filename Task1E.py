from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    number = int(input("enter a positive integer: "))
    stations = build_station_list()
    nstations = rivers_by_station_number(stations, number)
    print(nstations)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()