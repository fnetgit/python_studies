print(f"1. O Python leu o arquivo 'mod_teste'.")
print(f"2. O valor da variável __name__ aqui é: {__name__}")


def soma(x, y):
    return x + y


if __name__ == '__main__':
    print('--- INÍCIO DO BLOCO MAIN ---')
    print('3. Eu estou rodando DIRETO neste arquivo.')
    print(f'4. O resultado da soma é: {soma(5, 8)}')
    print('--- FIM DO BLOCO MAIN ---')
