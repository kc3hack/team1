import time_
import station
import root

def execute( latitude, longitude , food_name, per_time):
    count = 0
    if food_name == "たこ焼き":
        count = 0
    else:
        count = 1
    
    station_list = []
    shop = time_.execute( latitude, longitude, food_name )#shopの情報を取ってくる
    my_near_station = station.min_dist_station( latitude, longitude )#自分に一番近い駅の名前を取得
    ros = root.root_seach( my_near_station )
    
    for i in range( 0, per_time ):
        station_ = {}
        arrival_name = station.min_dist_station( float( shop[count][i]["latitude"] ), float( shop[count][i]["longitude"] ) )
        departure_time, arrival_time, spend_time = ros.time( arrival_name )
        station_["spend"] = spend_time
        station_["departure"] = my_near_station
        station_["arrival"] = arrival_name
        station_["url"] = shop[count][i]["url"]
        station_list.append( station_ )
        
    print( station_list )
    return station_list
execute( 34.982353, 135.961761, "たこ焼き", 5)
