# Funções lambda complexas

# Função executa:
# Recebe uma função e qualquer número de argumentos
# e retorna o resultado da função aplicada a esses argumentos.
def executa(funcao, *args):
    return funcao(*args)


# Exemplo 1: lambda que retorna outra lambda
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

# Exemplo 2: lambda com dois argumentos
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

# Exemplo 3: lambda com número variável de argumentos
print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
