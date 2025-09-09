# Introdução às Generator functions

# Uma "generator function" é como uma fábrica que produz iteradores.
# Ao ser chamada, ela não executa o código, apenas cria e retorna um objeto generator.
def generator_function(n=0, maximum=10):
    print('Generator criado! (O código interno ainda não rodou)')

    while n < maximum:
        # A palavra "yield" PAUSA a função aqui.
        # Ela retorna o valor atual de 'n' para quem a chamou.
        # O estado da função (variáveis locais) é congelado até a próxima chamada
        yield n

        # Quando o próximo valor é solicitado, a execução retoma DESTA LINHA.
        print(f'   (retomando com n valendo {n})')
        n += 1

    # Quando o laço termina, a função se encerra.
    # Isso dispara internamente uma exceção (StopIteration),
    # que simplesmente sinaliza para o 'for' que não há mais valores.
    print('Fim da execução do generator.')


# Como Usar

# Criando o objeto generator
# Neste momento, apenas a primeira linha do print dentro da função será executada.
gen = generator_function(maximum=3)
print('O laço "for" vai começar agora e pedir os valores')

# Consumindo os valores do generator
# A cada iteração, o 'for' pede um novo valor ao 'gen',
# Isso faz a função sair da pausa, rodar até o próximo 'yield' e pausar de novo for numero in gen:
for numero in gen:
    print(f'Laço "for" recebeu: {numero}')
