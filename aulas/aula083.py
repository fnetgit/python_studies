# Empacotamento e desempacotamento de dicionários + *args e **kwargs

pessoa = {
    'nome': 'Fulano',
    'sobrenome': 'Silva',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# Desempacotando os dois dicionários dentro de um novo
pessoa_completa = {**pessoa, **dados_pessoa}

# pessoa.items() retorna pares (chave, valor)
for chave, valor in pessoa_completa.items():
    print(chave, valor)
print('')
# *args    - empacota argumentos posicionais em uma tupla
# **kwargs - empacota argumentos nomeados (keyword arguments) em um dicionário


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS (args):', args)

    print('NOMEADOS (kwargs):')
    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(10, 20, nome='Joana', qlq=123)
print('')

# Desempacotando um dicionário diretamente como kwargs
mostro_argumentos_nomeados(**pessoa_completa)
print('')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
