# Tipos built-in, documentação, tipos imutáveis, métodos de string

# Tipos built-in (tipos embutidos): int, float, bool, str, list, tuple, set, dict
# * Tipos imutáveis: int, float, bool, str, tuple
# * Tipos mutáveis: list, set, dict

STRING = 'fco'
# STRING[3] = ' neto' # Dá erro, pois strings são imutáveis
STRING2 = f'{STRING.capitalize()} Neto'
print(STRING)   # fco
print(STRING2)  # Fco Neto

# Métodos de string: upper(), lower(), title(), capitalize(), strip(), split(), join(), replace(),
# find(), count(), index(), zfill()...
