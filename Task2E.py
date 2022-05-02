from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    #generate a station list and update the water levels
    stations = build_station_list()
    update_water_levels(stations)

#for the past 10 days... (dt is number of days)
    dt = 10
    #we find the 5 stations with the highest relative water level
    needed_stations = stations_highest_rel_level(stations,5)
    for i in needed_stations:
        for station in stations:
            if i[0].name == station.name:
                dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
                #we plot the levels against time
                plot_water_levels(station,dates,levels)
            else: 
                pass
        

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()