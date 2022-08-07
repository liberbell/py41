d = {"x": 10, "y": 20}
print(d, type(d))
print(d["x"], d["y"])

d["x"] = 100
print(d["x"], d["y"])
d["z"] = 200
print(d["x"], d["y"], d["z"])
d[1] = 1000
print(d)