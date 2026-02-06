# Enum - Enumerações

# Enums são usadas quando temos um conjunto FINITO de opções válidas.
# Enums têm membros, os quais tem nomes e valores constantes.

# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
# diretamente (mesmo assim, Enums não são classes normais).

# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.

# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# É melhor fazer com classe do que variável, porque...


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()  # gera um valor automaticamente, a partir do 1
    DIREITA = enum.auto()


print('Acessando membros:')
print(Direcoes(1))              # acessando pelo valor
print(Direcoes['ESQUERDA'])     # acesssando pelo nome
print(Direcoes.ESQUERDA, '\n')  # acessando o membro diretamente

print('Acessando propriedades:')
print(Direcoes.ESQUERDA.name,
      Direcoes.ESQUERDA.value,
      '\n')


# A função pede um valor do tipo Direcoes
def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção inválida')
    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
