# Funções dir, hasattr e getattr

# dir() lista todos os nomes de atributos e métodos que um determinado objeto possui.
# É uma ferramenta de exploração para descobrir o que você pode fazer com um objeto.

# hasattr() verifica se um objeto possui um atributo ou método com um nome específico.

# getattr() obtém um atributo ou método de um objeto usando seu nome em formato de string.
# É útil quando o nome do método que você quer chamar está guardado em uma variável.


string = 'Fco'
print(dir(string))

if hasattr(string, 'upper'):
    print("O objeto 'string' TEM o método 'upper'.")
else:
    print("O objeto 'string' NÃO TEM o método 'upper'.")


metodo_a_usar = 'upper'
metodo_real = getattr(string, metodo_a_usar)

resultado = metodo_real()

print(
    f"O resultado da chamada de getattr(string, '{metodo_a_usar}')() é: {resultado}")
