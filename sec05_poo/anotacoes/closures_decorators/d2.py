# Desafio 2: Closures (A Memória)

# Objetivo: Criar uma função que "lembra" de um dado configurado anteriormente. Tarefa: Crie uma função criador_de_multiplicadores(fator).

# Ela deve retornar uma função interna.
# A função interna deve receber um número x e retornar x * fator.
# Use isso para criar duas funções independentes: dobrar (fator 2) e triplicar (fator 3).

# Teste esperado:

# dobrar = criador_de_multiplicadores(2)
# triplicar = criador_de_multiplicadores(3)

# print(dobrar(10))   # Saída: 20
# print(triplicar(10)) # Saída: 30

def criador_de_multiplicadores(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar


dobrar = criador_de_multiplicadores(2)
triplicar = criador_de_multiplicadores(3)

print(dobrar(10))   # Saída: 20
print(triplicar(10))  # Saída: 30
