import requests

r = requests.post(
    "http://127.0.0.1:5000/post", data={"username": "Alex"}
)
print(r)