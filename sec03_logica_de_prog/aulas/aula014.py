# Formatação de strings com o método format

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# Usando parâmetros posicionais
string = 'b={1} a={1} a={0} c={2:.2f}'
formato = string.format(a, b, c)

# Usando parâmetros nomeados
string2 = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato2 = string2.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
print(formato2)
