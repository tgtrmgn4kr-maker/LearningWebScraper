from os import path
from pathlib import Path

f_path = path.join(Path(__file__).resolve().parent, 'momoshop_products.txt')

with open(f_path, 'r', encoding='utf-8') as f: #Safer way to open files
    content = f.readline()
    print(content)


