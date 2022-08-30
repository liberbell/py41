import urllib.request
import json

payloads = {"key1": "value1", "key2": "value2"}

url = "https://httpbin.org/get" + "?" + urllib.parse.urlencode(payloads)
url2 = "http://httpbin.org/get" + "?" + "?"

print(url)

# with urllib.request.urlopen(url) as url_open:
#     print(url_open.read().decode("utf-8"))
#     print(json.loads(url_open.read().decode("utf-8")))

# with urllib.request.urlopen(url2) as url_open:
#     print(url_open.read().decode("utf-8"))
    # print(json.loads(url_open.read().decode("utf-8")))

payloads = json.dump(payloads).encode("utf-8")
req = urllib.request.Request("https://httpbin.org/post", data=payloads, method="POST")