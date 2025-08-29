# Dicionários em Python (tipo dict)

# Estruturas de dados em pares "chave: valor"
# Chaves: tipos imutáveis (str, int, float, bool, tuple)
# Chaves podem ser consideradas como o "índice"

# Valores: qualquer tipo (int, str, list, dict, etc.)

# Usamos as chaves - {} - ou a classe dict para criar dicionários.


# pessoa = dict(nome='Francisco', sobrenome='Neto')

pessoa = {
    'nome': 'Francisco',
    'sobrenome': 'Neto',
    'idade': 19,
    'altura': 1.6,
    'endereços': [
        {'rua': 'tal tal', 'número': 13},
        {'rua': 'outra rua', 'número': 321},
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# deepcopy - retorna uma cópia profunda (deep copy). Precisa ser importado de copy
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
