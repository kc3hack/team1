import station
import requests
from bs4 import BeautifulSoup

class root_seach:
    def __init__(self, name):
        self.departure_name = name
        
    def time(self, arrival_name):
        url = "https://transit.yahoo.co.jp/search/result?flatlon=&from=" + self.departure_name + "&tlatlon=&to=" + arrival_name
        get_data = requests.get(url)
        soup =BeautifulSoup( get_data.text, "lxml")
        print(soup.find_all("li", class_ = "time")[0].text)
        print(soup.find_all("span", class_ = "mark")[0].text)
        print(soup.find_all("span", class_ = "small")[0].text)

rr = root_seach(station.min_dist_station(34.982353, 135.961761))
rr.time("大阪")
