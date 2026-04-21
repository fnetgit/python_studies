# sys.argv - lista de argumentos passados na linha de comando (argument vector)

import sys

# python3 aula187.py teste
argumentos = sys.argv
qtd_argumentos = len(argumentos)
print(argumentos)
print(qtd_argumentos)

if qtd_argumentos <= 1:
    print("Nenhum argumento foi passado")
elif qtd_argumentos == 3:
    print(f"Faça tal coisa com o argumento {argumentos[2]}")
else:
    print(f"Você passou os argumentos: {argumentos[1:]}")
