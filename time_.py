import math
import random
import api

def execute( current_latitude, current_longitude , food_name):
    shop_list = api.search( food_name )
    for i in range( 0, len( shop_list )):
        shop_list[i]["dist"] = min_dist( float( shop_list[i]["latitude"] ),  float( shop_list[i]["longitude"] ), current_latitude, current_longitude)
            
    shop_list.sort( key = lambda x: x["dist"])
    
    return shop_list
    
def min_dist( latitude1, longitude1, latitude2, longitude2 ):
    dist = math.sqrt( pow( ( latitude1 - latitude2), 2 ) + math.pow( (longitude1 - longitude2), 2 ) )
    earth_dist = 40000.0 * 1000 / 360#経度、緯度１度あたりのmの距離
    min_dist = dist * earth_dist
    return min_dist

