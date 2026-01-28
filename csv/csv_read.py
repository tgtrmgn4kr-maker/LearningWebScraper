import csv
from os import path
from pathlib import Path

p = path.join(Path(__file__).resolve().parent, 'sample.csv')

with open(p, 'r' ) as f:
    r = csv.reader(f)
    for row in r:
        print(type(row), row)

with open(p, 'r') as f:
    r= csv.DictReader(f)
    for row in r:
        print(type(row), row)