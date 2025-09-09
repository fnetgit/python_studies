# Como o for funciona por baixo dos panos?

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador 
"""

# "__" se chama dunder em Python

# ----------------------------------------
""" 
# texto = 'Fco'.__iter__()
texto1 = iter('Fco')  # mesma coisa do acima
print(texto1)
"""

# -----------------------------------------
""" 
print(texto1.__next__)
print(texto1.__next__)
print(texto1.__next__)
print(texto1.__next__)  # vai levantar um erro 
 """

# -----------------------------------------
texto2 = 'neto'  # iterável
iterador = iter(texto2)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# isso acima é o mesmo que o abaixo

for letra in texto2:
    print(letra)
