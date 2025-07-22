# while/else

# O else do while só executa se o laço terminar normalmente (ou seja, sem break).
i = 0
while i < 5:
    if i == 3:
        print("Parou no 3")
        break
    i += 1
else:
    print("Loop terminou normalmente")
