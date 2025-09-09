# Fatiamento de strings e a função len()

#  012345678 índices
#  Francisco palavra
# -987654321 índices

# Fatiamento [início:fim:passo]
# len()      Retorna a quantidade de caracteres da string

VAR = 'Francisco'

print(len(VAR))        # 9

print(VAR[0])             # F
print(VAR[-8])            # r
print(VAR[0:4])           # Fran
print(VAR[0:9:4])         # Fco
print(VAR[0:8])           # Francisc
print(VAR[0:9])           # Francisco
print(VAR[-9:])           # Francisco
print(VAR[:])             # Francisco
print(VAR[0:len(VAR):1])  # Francisco
print(VAR[-1:-10:-1])     # ocsnicarF
print(VAR[::-1])          # ocsnicarF
