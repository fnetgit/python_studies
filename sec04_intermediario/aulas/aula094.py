# try, except e finally

# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# Diferente do except que acontece se o try não funcionar o finally sempre executa

try:
    print(13/0)
    print(1)
except ZeroDivisionError:
    print(2)
else:
    # só é executado se o bloco try terminar sem nenhum erro.
    print(3)
finally:
    print(4)
