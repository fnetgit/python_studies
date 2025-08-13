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
    if len(user_input) < 1 or len(user_input) > 1 or len(user_input) == ' ':
        print("Digite APENAS uma letra.")
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
