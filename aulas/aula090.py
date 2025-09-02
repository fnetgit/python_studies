import sys

# Generator expression, Iterables e Iterators

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

# O generator é um tipo de iterator. Ele não armazena uma coleção de valores,
# mas sim uma "receita" ou "instrução" de como gerar o próximo valor
# apenas quando ele for solicitado.

# A diferença entre lista e generator é que...
# A lista guarda TODOS os valores na memória de uma só vez (é um container).
# Já o generator gera UM valor de cada vez, sob demanda. Após entregar um valor,
# ele o "esquece" e apenas guarda o estado para saber como gerar o próximo.
# Ele nunca possui todos os valores ao mesmo tempo.

# A prova está no uso de memória:
print(f'Memória da LISTA: {sys.getsizeof(lista)} bytes')
print(f'Memória do GENERATOR: {sys.getsizeof(generator)} bytes')
