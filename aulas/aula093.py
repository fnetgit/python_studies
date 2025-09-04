# try e except para tratar exceções pt.1

try:
    a = 18
    b = 0
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as error:
    print('Dividiu por zero.')
    print(f'MSG do erro: {error}')
    print(f'Nome do erro:{error.__class__.__name__}')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
# except Exception:
#     print('ERRO DESCONHECIDO.')
# Má prática
print('CONTINUAR')
print(__name__)
