import csv
import pprint
import object

with open('bun.csv', encoding="utf-8") as f:
    print(f.read())
    reader=csv.reader(f)
    for row in reader:
        print(row)
        puizu=Puizu()
        puizu.puizu=row()
        row(1)
