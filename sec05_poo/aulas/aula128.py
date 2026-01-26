# Métodos de classe + factories

# São métodos onde "self" será "cls", ou seja,
# em vez de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # método de classe
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod  # factory method
    def criar_com_80_anos(cls, nome):
        return cls(nome, 80)

    @classmethod  # factory method
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


Pessoa.metodo_de_classe()

p1 = Pessoa('Marco', 34)
p2 = Pessoa.criar_com_80_anos('Eliomar')

# Mesmas coisas
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
