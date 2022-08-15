from tkinter import Y


w = ["mon", "tue", "wed"]
f = ["coffee", "milk", "water"]

d = {}
for k, v in zip(w, f):
    d[k] = v

print(d)