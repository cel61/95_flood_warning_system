from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    rivers = []
    riverset = set()
    stations = build_station_list()
    riverswithstations = rivers_with_station(stations)
    for i in riverswithstations:
        riverset.add(i)
    for i in riverset:
        rivers.append(i)
    rivers.sort()
    result = rivers[0:10]
    print(result)
    rstations = stations_by_river(stations)
    aire = rstations[0]
    cam = rstations[1]
    thames = rstations[2]
    print("stations on river aire: ", aire)
    print("stations on river cam: ", cam)
    print("stations on river thames: ", thames)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()