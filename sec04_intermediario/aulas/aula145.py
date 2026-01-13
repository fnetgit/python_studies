# Aula adicionada posteriormente
# Positional-Only Parameters (/) e Keyword-Only Arguments (*)

# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)

# Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional (não nomeado).

def calcular_potencia(base, expoente, /):
    return base ** expoente


# FUNCIONA (apenas posição):
print(calcular_potencia(2, 3))

# QUEBRA (se tentar nomear):
# print(calcular_potencia(base=2, expoente=3))

# Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.


def formatar_texto(texto, *, maiusculo=False, centralizar=False):
    if maiusculo:
        texto = texto.upper()
    if centralizar:
        texto = texto.center(20)
    return texto


# FUNCIONA (argumentos nomeados após o texto):
print(formatar_texto("oi", maiusculo=True))

# QUEBRA (se tentar passar posicional):
# print(formatar_texto("oi", True))

# Resumo:
# Antes da /, só posicional
# Depois do *, só nome.
