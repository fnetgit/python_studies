# Introdução ao try/except

# try    -> Tentar executar o código
# except -> Ocorreu algum erro ao tentar executar

numero_str = input('Vou dobrar o número que você digitar: ').strip()

try:
    numero_float = float(numero_str)
    dobro = numero_float * 2
    print(f'O dobro de {numero_float:.2f} é {dobro:.2f}')
except:
    print('Isso não é um número')
