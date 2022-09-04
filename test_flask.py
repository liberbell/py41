import requests

r = requests.post(
    "http://127.0.0.1:5000/employee", data={"name": "Alex"}
)

r = requests.get(
    "http://127.0.0.1:5000/employee", data={"username": "Alex"}
)

print(r.text)