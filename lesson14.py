d = {"x": 10, "y": 20}
print(d, type(d))
print(d["x"], d["y"])

d["x"] = 100
print(d["x"], d["y"])
d["z"] = 200
print(d["x"], d["y"], d["z"])
d[1] = 1000
print(d)

d1 = dict(a=10, b=20)
print(d1)

d2 = dict([("a", 10), ("b", 20)])
print(d2)

d3 = {"x": 10, "y": 20}
print(d3.keys(), d3.values())

d4 = {"x": 1000, "j": 500}
d3.update(d4)
print(d3)