# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 's' in letras:
        print('saiu')
        break

    print(letras)
