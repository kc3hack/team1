from urllib import request, parse
import json

def search(word="たこ焼き"):
    with request.urlopen("https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=a8894c3975e74a3cba1b20e617663e8c&freeword="+parse.quote(word)) as res:
        html = res.read().decode("utf-8")
    a = json.loads(html)
    hoge = []
    for x in a["rest"]:
        hoge.append({"id":x["id"], "url": x["url"], "latitude": x["latitude"], "longitude": x["longitude"]})
    return hoge


if __name__ == '__main__':
    print(search())