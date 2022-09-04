import requests

r = requests.post(
    "http://127.0.0.1:5000/employee", data={"name": "Alex"}
)

r = requests.put(
    "http://127.0.0.1:5000/employee", data={"name": "Alex", "new_name": "Alexander"}
)

print(r.text)