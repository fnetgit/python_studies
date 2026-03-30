# random - geradores de números pseudoaleatórios

import random

# Define a semente para garantir a reprodutibilidade dos resultados
# normalmente a seed padrão é o horário do sistema,
# o que garante que os números gerados sejam diferentes a cada execução
# random.seed(0)

# Gera um número inteiro aleatório em um intervalo específico (exclusivo)
r_range = random.randrange(10, 19, 2)

# Gera um número inteiro aleatório entre 10 e 20 (inclusive)
r_int = random.randint(10, 20)

# Gera um número de ponto flutuante aleatório
r_uniform = random.uniform(10, 20)

nomes = ["Ana", "Bia", "Caio", "Duda"]
# Embaralha os elementos do iterável (modifica o iterável)
random.shuffle(nomes)
# print(nomes)

# Escolhe N elementos do iterável e retorna outro iterável (sem repetir valores)
novos_nomes1 = random.sample(nomes, k=3)
# print(novos_nomes1)

# Escolhe N elementos do iterável e retorna outro iterável (repete valores)
novos_nomes2 = random.choices(nomes, k=3)
# print(novos_nomes2)

# Escolhe um elemento aleatório do iterável
print(random.choice(nomes))
