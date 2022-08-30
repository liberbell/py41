import requests

payload = {"key1": "value1", "key2": "value2"}

url1 = "https://httpbin.org/get"

r = requests.get(url1, params=payload)
print(r.status_code)
print(r.text)