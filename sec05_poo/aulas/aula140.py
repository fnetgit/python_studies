# Herança Múltipla

# Quer dizer que uma classe pode estender várias outras classes.

# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente

# Herança múltipla e mixins(classe que só serve para "compor" outras classes):
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)


# Herança múltipla pode causar o Problema do diamante
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
#  Supondo que o método falar exista em A, B e C sobrescrevam esse método.
#  Quando chamamos D.falar(), qual método será executado?
#  O Python vai usar a MRO.

#           A
#         /   \
#        B     C
#         \   /
#           D

# a MRO usa o algoritmo C3 Linearization para definir a ordem de busca dos métodos.
# 1. Esquerda para a Direita: Se definiu D(B, C), B tem prioridade sobre C.
# 2. Especificidade: Filhos têm prioridade sobre Pais.

# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__
