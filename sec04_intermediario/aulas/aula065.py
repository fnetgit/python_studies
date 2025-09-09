"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# Parâmetros: São as variáveis definidas na declaração de uma função.
# Argumentos: São os valores reais passados para os parâmetros quando a função é chamada.


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Fco')
saudacao('Neto')
saudacao()  # valor padrão "Sem nome"
