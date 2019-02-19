import math
import time
import glob

def min_dist_station( la, lo ):
    station_data = station_list()

    for i in range( 0, len( station_data ) ):
        station_data[i]["dist"] = min_dist( la, lo,  station_data[i]["point"][0], station_data[i]["point"][1] )
        
    station_data.sort( key = lambda x: x["dist"] )
    return station_data[0]["name"]
        
def min_dist( la, lo, latitude, longitude ):
    dist = math.sqrt( math.pow( ( la - latitude), 2 ) + math.pow( ( lo - longitude ), 2 ) )
    earth_dist = 40000.0 * 1000 / 360#経度、緯度１度あたりのmの距離
    min_dist = dist * earth_dist
    return min_dist

def station_list():
    file_name = "station_list.txt"
    station_main = []
        
    f = open( file_name )
    station_data = f.readlines()
        
    for i in range( 0, len( station_data ) ):
        station_place = {}
        station_data[i] = station_data[i].replace("\n", "")
        station = station_data[i].split(",")
        x_y = ( float( station[1] ), float( station[2] ) )
        station_place["name"] = station[0]
        station_place["point"] = x_y
        station_main.append( station_place )

    return station_main
