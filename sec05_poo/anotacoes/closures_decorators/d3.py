# Desafio 3: O Decorator "Dedo-Duro" (Básico)

# Objetivo: Interceptar a execução de uma função. Tarefa: Crie um decorator chamado @avisar_inicio.

# Antes de executar a função decorada, ele deve printar: "Atenção: A função [NOME_DA_FUNCAO] vai rodar agora.".
# Depois, ele executa a função original normalmente. Dica: Use func.__name__ para pegar o nome.

# Teste esperado:

# @avisar_inicio
# def somar(a, b):
#     print(f"Soma: {a + b}")

# somar(5, 5)

# # Saída esperada:
# # Atenção: A função somar vai rodar agora.
# # Soma: 10

def avisar_inicio(func):
    def wrapper(*args, **kwargs):
        print(f"Atenção: A função {func.__name__} vai rodar agora.")
        func(*args, **kwargs)
    return wrapper


@avisar_inicio
def somar(a, b):
    print(f"Soma: {a + b}")


somar(5, 5)
# A função original deixa de existir e o wrapper a substitui, por isso ali o wrapper
# precisou de * e **


# Decorator é uma função que recebe uma função como parâmetro e dentro dela cria um wrapper
# que faz o que eu quero que o decorator faça e depois executa a função que ele recebe como parâmetro.
# Logo um decorator pode atribuir uma nova funcionalidade a uma função.
