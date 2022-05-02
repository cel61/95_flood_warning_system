from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    #create a list of stations

    stations = build_station_list()
    tol = 0.8
    #tolerance is 0.8

    update_water_levels(stations)

    #find all stations with a relative water level within their relative range of over 0.8
    
    result = stations_level_over_threshold(stations, tol)
    for i in result:
        print(i[0].name,i[1])
    



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()