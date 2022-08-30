import requests

payload = {"key1": "value1", "key2": "value2"}

url1 = "https://httpbin.org/get"
url1 = "https://httpbin.org/get"

# r = requests.get(url1, params=payload)
r = requests.post(url1, data=payload)

print(r.status_code)
print(r.text)
# print(r.json())