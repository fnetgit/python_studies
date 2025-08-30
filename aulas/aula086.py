# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()                  # Se o valor for string, converte para maiúsculo
    if isinstance(valor, str) else valor  # Se não for string, mantém como está
    for chave, valor                      # Desempacota cada par chave, valor
    in produto.items()                    # Percorre os pares (chave, valor) do dicionário produto
    if chave != 'categoria'               # Filtra: ignora a chave 'categoria'
}
# isinstance() explicado na próxima aula

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)
