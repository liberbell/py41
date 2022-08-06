seat = []
min = 0
max = 4
print(min <= len(seat) < max)

seat.append("p")
print(min <= len(seat) < max)

seat.append("q")
print(min <= len(seat) < max)

seat.append("r")
print(min <= len(seat) < max)

seat.append("s")
print(min <= len(seat) < max)

seat.pop(0)
print(seat)
print(min <= len(seat) < max)