# Desafio 4: O Decorator de Caixa Alta (Modificando Retorno)

# Objetivo: Alterar o que sai de uma função sem tocar no código dela. Tarefa: Crie um decorator @tudo_maiusculo.

# Ele deve decorar qualquer função que retorne uma string.
# Ele pega o retorno original, transforma em UPPERCASE e retorna o novo valor.

# Teste esperado:

# @tudo_maiusculo
# def get_nome_usuario():
#     return "francisco neto"

# print(get_nome_usuario())
# Saída esperada: FRANCISCO NETO

def tudo_maiusculo(func):
    def wrapper():
        return func().upper()
    return wrapper


@tudo_maiusculo
def get_nome_usuario():
    return "francisco neto"


print(get_nome_usuario())