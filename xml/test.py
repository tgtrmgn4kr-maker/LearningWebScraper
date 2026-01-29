import xmltodict as xd
from os import path
from pathlib import Path

p = path.join((Path(__file__).resolve().parent), 'Keelung_air.xml')

with open(p, 'r', encoding='utf-8') as f:
    doc = xd.parse(f.read())

for k, v in doc.items():
    print(f'{k}: {v}\n')


























