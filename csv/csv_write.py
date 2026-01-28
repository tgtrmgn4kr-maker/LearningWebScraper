import csv
from os import path
from pathlib import Path

s_path = path.join(Path(__file__).resolve().parent, 'sample.csv')

titles = ['apple', 'banana', 'cherry']
prices = ['$100', '$200', '$300']

with open(s_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Title', 'Price'])
    for title, price in zip(titles, prices):
        w.writerow([title, price])
















