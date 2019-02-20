import math
import random
import api

def execute( current_latitude, current_longitude , food_name):
    #shop_list = api.search( food_name )
    count = 0
    if food_name == "たこ焼き":
        count = 0
    else:
        count = 1
    shop_list = api.load()
    
    for i in range( 0, len( shop_list[count] )):
        if len( shop_list[count][i]["latitude"] ) == 0\
           or len( shop_list[count][i]["longitude"] ) == 0:
            
            shop_list[count][i]["dist"] = 100000000
        else:
            shop_list[count][i]["dist"] = min_dist( float( shop_list[count][i]["latitude"] ),  float( shop_list[count][i]["longitude"] ), current_latitude, current_longitude)
            
    shop_list[count].sort( key = lambda x: x["dist"])
    
    return shop_list
    
def min_dist( latitude1, longitude1, latitude2, longitude2 ):
    dist = math.sqrt( pow( ( latitude1 - latitude2), 2 ) + math.pow( (longitude1 - longitude2), 2 ) )
    earth_dist = 40000.0 * 1000 / 360#経度、緯度１度あたりのmの距離
    min_dist = dist * earth_dist
    return min_dist

