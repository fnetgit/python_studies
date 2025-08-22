"""
Escopo de funções em Python pt.2

Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra 'global' faz uma variável do escopo externo 
ser a mesma no escopo interno.
Usar 'global' pode ser uma má prática.
"""

# Escopo Global
x = 9


def escopo():
    # Escopo Local da função 'escopo'

    # Ao atribuir 'x = 10' sem a palavra-chave 'global', criamos uma NOVA
    # variável 'x' que existe APENAS dentro desta função.
    # Ela não afeta o 'x' global. Dizemos que ela "sombra" a global.
    x = 10

    def outra_funcao():
        # Escopo Local da função 'outra_funcao'

        # Novamente, uma NOVA variável 'x' é criada, local.
        x = 15
        y = 4

        # Imprime o 'x' do escopo mais próximo (local de outra_funcao), que é 15.
        print(f"Dentro de outra_funcao: x={x}, y={y}")

    outra_funcao()

    # Ao final de 'outra_funcao', seu 'x=15' é destruído.
    # Agora, este print usa o 'x' do seu próprio escopo (local de escopo), que é 10.
    print(f"Dentro de escopo, após outra_funcao: x={x}")


# Imprime o 'x' do escopo global.
print(f"Antes de chamar escopo (global): x={x}")

escopo()

# A função 'escopo' terminou e sua variável local 'x=10' foi destruída.
# Logo, acessa o 'x' global
print(f"Depois de chamar escopo (global): x={x}")
