from urllib import request, parse
import json

def search(word="たこやき"):
    hoge = []
    for i in range(1, 100000):
        try:
            with request.urlopen(f"https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=a8894c3975e74a3cba1b20e617663e8c&hit_per_page=100&offset_page={i}&freeword={parse.quote(word)}") as res:
                html = res.read().decode("utf-8")
        except:
            break
        a = json.loads(html)
        for x in a["rest"]:
            hoge.append({"id":x["id"], "url": x["url"], "latitude": x["latitude"], "longitude": x["longitude"]})
    return hoge


if __name__ == '__main__':
    print(len(search()))