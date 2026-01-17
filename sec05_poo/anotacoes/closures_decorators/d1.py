# Desafio 1: Funções Aninhadas (O Escopo)

# Objetivo: Entender que funções internas "enxergam" variáveis da função pai. Tarefa: Crie uma função chamada calculadora_impostos(valor_base).

# Dentro dela, defina uma função aninhada chamada calcular_iss() que calcula 5% do valor_base.
# Defina outra aninhada calcular_icms() que calcula 10% do valor_base.
# A função pai deve retornar a soma do valor base + os dois impostos.

# Teste esperado:

# print(calculadora_impostos(100))
# Saída esperada: 115.0

def calculadora_impostos(valor_base):
    def calcular_iss():
        return valor_base * 0.05

    def calcular_icms():
        return valor_base * 0.10
    return valor_base + calcular_iss() + calcular_icms()

print(calculadora_impostos(100))
