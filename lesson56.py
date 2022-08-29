import json

j = {
    "employee":
    [
        {"id": 111, "name": "Eric"},
        {"id": 222, "name": "Alex"}
    ]
}

print(j)
print("####")
print(json.dumps(j))