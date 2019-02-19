import time_
import station
import root

def execute( latitude, longitude , food_name, per_time):
    shop = time_.execute( latitude, longitude, food_name )#shopの情報を取ってくる
    my_near_station = station.min_dist_station( latitude, longitude )#自分に一番近い駅の名前を取得
    ros = root.root_seach( my_near_station )
    
    for i in range( 0, len( shop ) ):
        arrival_name = station.min_dist_station( float( shop[i]["latitude"] ), float( shop[i]["longitude"] ) )
        departure_time, arrival_time, spend_time = ros.time( arrival_name )
        shop[i]["time"] = spend_time
        print(spend_time)
    shop.sort(key = lambda x: x["time"])
    print(shop[0:3])
execute( 34.982353, 135.961761, "たこやき", 30)
