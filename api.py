from urllib import request, parse
import json
from concurrent.futures import ThreadPoolExecutor
import itertools
import pickle

API_KEY = "041bf926060de0bdcbe537265b4c78ea"

def search(word="たこ焼き"):
    def foo(area):
        fuga = []
        for i in range(1, 100000):
            try:
                with request.urlopen(f"https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={API_KEY}&hit_per_page=100&areacode_l={area}&offset_page={i}&freeword={parse.quote(word)}&freeword_condition=2") as res:
                    # ','.join(word)
                    html = res.read().decode("utf-8")
            except Exception as e:
                break
            a = json.loads(html)
            for x in a["rest"]:
                if x["latitude"]=="" or x["longitude"]=="": continue
                fuga.append({"id":x["id"], "url": x["url"], "latitude": x["latitude"], "longitude": x["longitude"]})
        return fuga
    pool = ThreadPoolExecutor(max_workers=32)
    with request.urlopen(f"https://api.gnavi.co.jp/master/GAreaLargeSearchAPI/v3/?keyid={API_KEY}") as res:
        html = res.read().decode("utf-8")
    result = pool.map(foo, [x["areacode_l"] for x in json.loads(html)["garea_large"]])
    hoge = list(itertools.chain.from_iterable(result))
    return hoge


if __name__ == '__main__':
    # print(len(search("たこ焼き")))
    with open('takoyaki.pickle', mode='wb') as f:
        pickle.dump(search("たこ焼き"), f)
    with open('okonomiyaki.pickle', mode='wb') as f:
        pickle.dump(search("お好み焼き"), f)

