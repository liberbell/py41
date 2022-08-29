import urllib.request
import json

url = "https://httpbin.org/get"
url2 = "http://httpbin.org/get"

# with urllib.request.urlopen(url) as url_open:
#     print(url_open.read().decode("utf-8"))
#     print(json.loads(url_open.read().decode("utf-8")))

with urllib.request.urlopen(url2) as url_open:
    print(url_open.read().decode("utf-8"))
    print(json.loads(url_open.read().decode("utf-8")))