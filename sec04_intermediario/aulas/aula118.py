# Errado
def adiciona_errado(nome, lista=[]):
    lista.append(nome)
    return lista


c1 = adiciona_errado('Luiz')
c2 = adiciona_errado('Maria')

# O problema: A Maria entrou na lista do Luiz!
print(c1)  # ['Luiz', 'Maria']
print(c2)  # ['Luiz', 'Maria']


# Certo
def adiciona_clientes(nome, lista=None):
    # Se não passou lista, cria uma NOVA agora
    if lista is None:
        lista = []

    lista.append(nome)
    return lista


# Teste 1: Criando do zero (lista é None -> vira [])
cliente1 = adiciona_clientes('Luiz')
print(cliente1)  # ['Luiz']

# Teste 2: Criando outro do zero (lista é None -> vira OUTRA [])
cliente2 = adiciona_clientes('Maria')
print(cliente2)  # ['Maria']

# Teste 3: Usando uma lista que já existe
adiciona_clientes('Joana', cliente1)
print(cliente1)  # ['Luiz', 'Joana']
