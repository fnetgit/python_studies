# __dict__ e vars para atributos de instância

# __dict__ : Atributo. Acesso direto à propriedade. Permite alterar valores E substituir o dicionário inteiro
# ex: p1.__dict__ = {}

# vars()   : Função built-in. Retorna o __dict__. Permite alterar valores internos, mas NÃO aceita atribuição direta à chamada
# ex: vars(p1) = {} dá ERRO
# ex2: vars(p1)['nome'] = 'Outro nome' funciona

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# p1 = Pessoa('Fco', 20)
dados = {'nome': 'Fco', 'idade': 20}
p1 = Pessoa(**dados)

print(p1.__dict__)  # {'nome': 'Fco', 'idade': 20}
p1.nome = 'Francisco'  # Alterando atributo

# dict é um dicionário que guarda os atributos de instância
print(p1.__dict__)             # {'nome': 'Francisco', 'idade': 20}
p1.__dict__['outra'] = 'coisa'  # Adicionando atributo dinamicamente
p1.__dict__['nome'] = 'Neto'   # Alterando atributo dinamicamente
# del p1.__dict__['nome']


print(vars(p1))
