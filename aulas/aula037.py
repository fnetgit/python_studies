# Pulando repetições com continue e break

# continue (interrompe a iteração atual do loop e imediatamente pula para a próxima iteração)
# break (interrompe o loop completamente)

counter = 0

while counter <= 100:
    counter += 1

    if counter == 3:
        print('Não vou mostrar o 3.')
        continue

    if counter >= 10 and counter <= 30:
        print('Não vou mostrar o', counter)
        continue

    print(counter)

    if counter == 40:
        break


print('Acabou')
