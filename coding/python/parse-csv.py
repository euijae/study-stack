import csv

with open("../file/example-simplify.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['City'])