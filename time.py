import math

def min_dist(latitude1, longitude1, latitude2, longitude2):
    dist = math.sqrt( pow( ( latitude1 - latitude2), 2 ) + math.pow( (longitude1 - longitude2), 2 ) )
    earth_dist = 40000.0 * 1000 / 360#経度、緯度１度あたりのmの距離
    min_dist = dist * earth_dist
    return min_dist


