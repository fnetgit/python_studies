"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.

ex.:
Selecione uma opção
[i]nserir [a]pagar [l]istar:
 """

items = []
while True:
    print('Selecione uma opção')
    user_input = input('[i]nserir [a]pagar [l]istar: ').lower()
    if user_input == 'i':
        item_to_insert = input('Valor: ')
        items.append(item_to_insert)
    elif user_input == 'l':
        if not items:
            print('A lista está vazia.')
        else:
            for idx, name in enumerate(items):
                print(idx, name)
    elif user_input == 'a':
        if not items:
            print('A lista está vazia.')
            continue
        try:
            index_to_delete = int(input('Escolha o índice para apagar: '))
            if 0 <= index_to_delete < len(items):
                items.pop(index_to_delete)
                print('item deletado com sucesso.')
            else:
                print('Não foi possível apagar esse índice.')
        except ValueError:
            print('Digite um número inteiro.')
    else:
        print('Digite uma opção válida.')

# Resposta
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
