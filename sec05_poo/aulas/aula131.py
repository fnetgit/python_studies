# @property - um getter no modo Pythônico

# getter - um método para obter um atributo
# cor -> get_cor()

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo

# Geralmente é usada nas seguintes situações:
# - como getter
# - evitar quebrar código cliente(código que usa seu código)
# - habilitar setter
# - executar ações ao obter um atributo


# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta


# caneta = Caneta('Azul')
# print(caneta.get_cor())

###################################

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
