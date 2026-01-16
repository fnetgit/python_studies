# Ler os dados de aula127_a.py

import json
import os
from aula127_a import Person

FOLDER_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.join(FOLDER_PATH, 'data.json')


with open(FILE_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

for p_dict in data:
    person = Person(**p_dict)
    print(person.name, person.age)
