# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
import os

FOLDER_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.join(FOLDER_PATH, 'data.json')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Fco', 20)
p2 = Person('Melissa', 19)

data = [p1.__dict__, p2.__dict__]

def save():
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )


if __name__ == '__main__':
    save()
