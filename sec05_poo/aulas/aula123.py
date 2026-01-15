# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão' # Atributo de classe

    def __init__(self, nome):
        self.nome = nome  # Atributo de instância

        variavel = 'valor'  # Variável local do método
        print(variavel)

    def comendo(self, alimento):  # Método da classe
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')    # Instância da classe Animal
print(leao.nome)              # Acessando o atributo de instância
print(leao.comendo('carne'))  # Usando o método da instância
print(leao.executar('maçã'))  # Usando o método da instância que chama outro método da instância
