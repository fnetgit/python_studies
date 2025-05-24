# id, Flags, is, is not e None

# A função id() retorna um identificador único para um objeto.
# Este identificador é o endereço do objeto na memória (CPython).
# Útil para verificar se duas variáveis se referem exatamente ao mesmo objeto.

a = [1, 2, 3]       # 'a' é uma lista
b = a               # 'b' agora aponta para o MESMO objeto que 'a'
c = [1, 2, 3]       # 'c' é uma NOVA lista, com o mesmo conteúdo de 'a'

print(f"id(a): {id(a)}")  # Mostra o identificador de 'a'
print(f"id(b): {id(b)}")  # Mesmo identificador de 'a'
print(f"id(c): {id(c)}")  # Identificador diferente de 'a' e 'b'


# Flags - Variáveis de Sinalização/Controle
# "Flags" (ou sinalizadores) são variáveis, geralmente booleanas (True/False),
# usadas para guardar um estado ou condição que pode mudar durante a execução
# do programa e controlar o fluxo (ex: em estruturas if/else).

condicao_satisfeita = False  # Flag inicializada como False

condicao = False
if condicao:
    print('Condição da flag é verdadeira')
else:
    print('Condição da flag é falsa')

idade_usuario = 10
if idade_usuario >= 8:
    condicao_satisfeita = True
if condicao_satisfeita:
    print("Acesso permitido pela flag.")
else:
    print("Acesso negado pela flag.")


# Operadores de Identidade
# is     -> Retorna True se duas variáveis apontam para o MESMO objeto na memória.
# is not -> Retorna True se duas variáveis NÃO apontam para o mesmo objeto.

# Diferença crucial:
# 'is' compara a IDENTIDADE dos objetos (se são o mesmo objeto).
# '==' compara os VALORES dos objetos (se têm o mesmo conteúdo).

lista_original = [10, 20, 30]
referencia_lista = lista_original      # Aponta para o mesmo objeto
copia_lista = [10, 20, 30]             # Novo objeto, mesmo conteúdo


print(
    # True
    f"lista_original is referencia_lista: {lista_original is referencia_lista}")

print(
    # True (valores são iguais)
    f"lista_original == referencia_lista: {lista_original == referencia_lista}")

# False (objetos diferentes)
print(f"lista_original is copia_lista: {lista_original is copia_lista}")

# True (valores são iguais)
print(f"lista_original == copia_lista: {lista_original == copia_lista}")

# Para tipos imutáveis pequenos (como inteiros pequenos e strings curtas),
# Python pode reutilizar objetos, então 'is' pode dar True:
num1 = 13
num2 = 13
print(f"num1 = {num1}, num2 = {num2}, num1 is num2? {num1 is num2}")

str1 = "ola"
str2 = "ola"
print(f"str1 = '{str1}', str2 = '{str2}', str1 is str2? {str1 is str2}")


# None -> É um objeto especial que representa a ausência de um valor,
# ou um valor "nulo", "vazio" ou "indefinido".
# Funções que não retornam explicitamente um valor, retornam None.

valor_config = None  # Inicializando uma variável que pode ou não receber um valor

if valor_config is None:
    print("Configuração não definida, usando valor padrão.")
    valor_config = "padrão"
else:
    print(f"Configuração definida: {valor_config}")
