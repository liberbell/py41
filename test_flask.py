import requests

r = requests.post(
    "http://127.0.0.1:5000/put", data={"username": "Alex"}
)
print(r.text)