# Herança simples

# Em Python, todas as classes são derivadas de 'object', mesmo que não declarado explicitamente.

# Primeiro o Python procura o método na própria classe,
# depois na superclasse (herança simples).

# o primeiro falar_nome_classe a ser executado será o da classe Cliente,
# pois ela sobrescreve o método da superclasse Pessoa.

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'


c1 = Cliente('Fco', 'Neto')
c1.falar_nome_classe()
a1 = Aluno('João', 'Silva')
a1.falar_nome_classe()
print(a1.cpf)

# Com o help é possível ver a hierarquia de classes, a Method Resolution Order (MRO)
# help(Cliente)
