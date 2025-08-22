"""
Escopo de funções em Python pt.1

Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""


x = 5


def escopo():
    global x
    x = 50

    def outra_funcao():
        global x
        x = 22
        y = 3
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
