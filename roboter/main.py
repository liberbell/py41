# import os
import csv

name_input = input("Hello. I am Roboko. What is your name?")
recom_input = input("{}, Which restaurants do you like?".format(name_input))
print(recom_input)

count = 0
with open("ranking.csv", "w") as rank_csv:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(rank_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow["Name": recom_input, "Count": count]