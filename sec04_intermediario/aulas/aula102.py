# Variáveis livres + nonlocal (locals, globals)

# Variável livre quando não está definida dentro do escopo de uma função dentro de outra

# print(globals())                    para ver as variáveis globais
# print(locals())                     para ver as variáveis locais
# print(escopo.__code__.co_freevars)  para ver as variáveis livres

# closure
def fora(x):
    a = x

    def dentro():
        print(dentro.__code__.co_freevars)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        # se não tiver nonlocal dá erro! Porque a veriavel nao é desse escopo,
        # só posso lê-la e não alterá-la
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
