"""
Closure e funções que retornam outras funções
"""

# Um closure acontece quando uma função interna (definida dentro de outra função) lembra do ambiente em que foi criada, mesmo depois que a função externa já terminou de executar.
# Ou seja: a função interna carrega consigo as variáveis locais da função externa.


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
