import csv

with open("test.csv", "w")as csv_file:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "A", "Count": "1"})
    writer.writerow({"name": "B", "Count": "2"})