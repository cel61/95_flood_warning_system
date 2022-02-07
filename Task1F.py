from floodsystem.geo import inconsistent_typical_range_stations
from floodsystem.geo import typical_range_consistent
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    result = inconsistent_typical_range_stations(stations)
    print(result)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()