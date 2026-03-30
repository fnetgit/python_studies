# secrets

import secrets

random = secrets.SystemRandom()
# Usa o gerador de números aleatórios do sistema operacional
# por isso o seed não funciona
# Com isso dá pra usar os métodos do módulo random, mas com a segurança do módulo secrets

rang = random.randint(10, 100)
print(rang)

print(secrets.randbelow(10))  # Gera um número inteiro aleatório entre 0 e 9
print(secrets.choice("Python"))


# Gerar uma senha aleatória

# import string as s
# from secrets import SystemRandom as Sr

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
