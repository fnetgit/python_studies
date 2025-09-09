# Recarregando módulos, importlib e singleton

# 1. Imports como Singleton: Por padrão, um módulo é carregado na memória
#    apenas uma vez, não importa quantas vezes ele seja importado. Python
#    armazena os módulos carregados em um dicionário chamado `sys.modules`.
#    Isso garante que todos os pontos do programa compartilhem a MESMA
#    instância do módulo, otimizando a memória e mantendo um estado consistente.
#
# 2. Recarregamento dinâmico: A função `importlib.reload()` permite forçar
#    a reexecução do código de um módulo já carregado. Isso é útil
#    principalmente em desenvolvimento e depuração, para aplicar alterações
#    em um módulo sem precisar reiniciar todo o programa.

import aula098_m

import importlib

print(aula098_m.VAR)

for i in range(10):
    importlib.reload(aula098_m)
    print(i)

print('Fim')
