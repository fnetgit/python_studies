# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
#
# _ (um underline) = protected
#       só DEVE ser usado na classe em que foi
#       declarado e nas classes que a herdam
#
# __ (dois underlines) = private
#       só DEVE ser usado na classe em que foi declarado.
#       usar __ ativa o "name mangling" (desfiguração de nomes), altera o nome de atributos ou métodos
#       ex.: _NomeClasse__nome_attr_ou_method

class Exemplo:
    def __init__(self):
        self.public = 'atributo público'
        self._protected = 'atributo protegido'
        self.__private = 'atributo privado'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


x = Exemplo()
# print('name mangling: ', x._Exemplo__metodo_private()) # acessando método private via name mangling, não recomendado
print(x.public)
print(x.metodo_publico())
