import requests

payload = {"key1": "value1", "key2": "value2"}

url1 = "https://httpbin.org/get"
url2 = "https://httpbin.org/post"
url3 = "https://httpbin.org/put"

# r = requests.get(url1, params=payload)
# r = requests.post(url2, data=payload)
r = requests.put(url3, data=payload)

print(r.status_code)
print(r.text)
print(r.json())