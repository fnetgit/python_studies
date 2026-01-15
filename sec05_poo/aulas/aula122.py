# Entendendo self em classes

# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados

# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar() # Usando o método pela instância
Carro.acelerar(fusca) # Usando o método pela classe, passando a instância como argumento
