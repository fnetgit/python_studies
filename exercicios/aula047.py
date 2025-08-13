"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.


ex.:

Digite uma letra: a
Palavra formatada: *******
Digite uma letra: e
Palavra formatada: *e****e
"""

# tentativa 1
secret_word = 'palavra'
formatted_word = ['*'] * len(secret_word)
tries = 0

while formatted_word != secret_word:
    user_input = input('Digite uma letra: ').lower()
    if len(user_input) < 1 or len(user_input) > 1 or user_input == ' ':
        print("Digite UMA letra.")
        continue
    tries += 1
    for i in range(0, len(secret_word)):
        if secret_word[i] == user_input:
            formatted_word[i] = user_input
            ''.join(formatted_word)
    print(''.join(formatted_word))
    if ''.join(formatted_word) == secret_word:
        print(f'Parabéns, a palavra era: "{secret_word}"')
        print(f'Você gastou {tries} tentativas.')
        break


# melhorando
secret_word = 'palavra'
formatted_word = ['*'] * len(secret_word)
tries = 0

while True:
    user_input = input('Digite uma letra: ').lower()
    if len(user_input) != 1 or not user_input.isalpha():
        print("Digite APENAS uma letra do alfabeto.")
        continue
    tries += 1
    if user_input in formatted_word:
        print("Você já adivinhou essa letra. Tente outra.")
        continue

    letter_found = False
    for i in range(len(secret_word)):
        if secret_word[i] == user_input:
            formatted_word[i] = user_input
            letter_found = True
    if not letter_found:
        print(f"A letra '{user_input}' não está na palavra. Tente novamente.")

    current_word = ''.join(formatted_word)
    print(current_word)

    if current_word == secret_word:
        print(f'Parabéns, a palavra era: "{secret_word}"')
        print(f'Você gastou {tries} tentativas.')
        break


# resposta
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
