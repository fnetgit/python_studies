import json

pessoa = {
    'nome': 'Francisco',
    'sobrenome': 'Neto',
    'enderecos': [
        {'rua': 'R1', 'numero': 13},
        {'rua': 'R2', 'numero': 15},
    ],
    'altura': 1.62,
    'numeros_preferidos': (2, 4, 6, 8, 10), # tupla será convertida para lista no json
    'dev': True,
    'nada': None,
}

# Escrevendo o arquivo json
with open('sec04_intermediario/aulas/aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False, # para aceitar caracteres especiais
        indent=2,
    )

# Lendo o arquivo json
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
