import os
import csv

file=os.path.join("Resources","budget_data.csv")

with open(file)as data:
    reader=csv.reader(data)
    for line in reader:
        print(line)