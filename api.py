from urllib import request, parse
import json
from concurrent.futures import ThreadPoolExecutor
import itertools
import pickle

API_KEY = "3fcdbaa2b34fc211c86ceddeb1b7ab8c"

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

def save():
    with open('takoyaki.pickle', mode='wb') as f:
        pickle.dump(search("たこ焼き"), f)
    with open('okonomiyaki.pickle', mode='wb') as f:
        pickle.dump(search("お好み焼き"), f)

def load():
    with open('takoyaki.pickle', mode='rb') as f:
        a = pickle.load(f)
    with open('okonomiyaki.pickle', mode='rb') as f:
        b = pickle.load(f)
    return a, b

if __name__ == '__main__':
    save()
    print(len(load()[0]))
    print(len(load()[1]))

