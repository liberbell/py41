print(globals())

# builtins.print()

ranking = {
    "A": 100,
    "B": 85,
    "C": 90
}

for key in ranking:
    print(key)

print(sorted(ranking, key=ranking.get))