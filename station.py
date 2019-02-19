import math
import time
import glob

class station_search:
    def __init__(self, latitude, longitude):
        self.la = latitude
        self.lo = longitude

    def min_dist_station( self ):
        station_data = self.station_list()

        for i in range( 0, len( station_data ) ):
            station_data[i]["dist"] = self.min_dist( station_data[i]["point"][0], station_data[i]["point"][1] )

        station_data.sort( key = lambda x: x["dist"] )
        print(station_data[0]["name"])
        
    def min_dist( self, latitude, longitude ):
        dist = math.sqrt( math.pow( ( self.la - latitude), 2 ) + math.pow( ( self.lo - longitude ), 2 ) )
        earth_dist = 40000.0 * 1000 / 360#経度、緯度１度あたりのmの距離
        min_dist = dist * earth_dist
        return min_dist

    def station_list( self ):
        file_list = glob.glob("station_list/*.txt")
        station_main = []
        
        for i in range( 0, len(file_list) ):
            f = open( file_list[i] )
            station_data = f.readlines()
            
            for r in range( 0, len( station_data ) ):
                station_place = {}
                station_data[r] = station_data[r].replace("\n", "")
                station = station_data[r].split(",")
                x_y = ( float( station[1] ), float( station[2] ) )
                station_place["name"] = station[0]
                station_place["point"] = x_y
                station_main.append( station_place )

        return station_main

s = station_search( 34.981367, 135.961507 )
s.min_dist_station()
