import imp
import urllib.request
import json

url = "https://httpbin.org/get"

with urllib.request.urlopen(url) as url_open:
    print(url_open.read().decode("utf-8"))