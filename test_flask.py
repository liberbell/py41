import requests

r = requests.get(
    "http://127.0.0.1:5000/employee/Alex"
)
print(r.text)

r = requests.post(
    "http://127.0.0.1:5000/employee", data={"name": "Alex"}
)
print(r.text)

r = requests.put(
    "http://127.0.0.1:5000/employee", data={"name": "Alex", "new_name": "Alexander"}
)
print(r.text)

r = requests.delete(
    "http://127.0.0.1:5000/employee", data={"name": "Alex"}
)
print(r.text)
