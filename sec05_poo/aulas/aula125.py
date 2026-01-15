# Atributos de Classe

class Produto:
    # Fica fora do __init__. É compartilhado por todos.
    taxa_imposto = 1.10

    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    def calcular_preco_final(self):
        return self.preco_base * Produto.taxa_imposto


mouse = Produto("Mouse Attack shark promoção", 99)
bombons = Produto("Caixa de bombons", 12)

print(f"Mouse com imposto: R$ {mouse.calcular_preco_final():.2f}")
print(f"Bombons com imposto: R$ {bombons.calcular_preco_final():.2f}")

print("-" * 30)
Produto.taxa_imposto = 1.50

print(f"Mouse com novo imposto: R$ {mouse.calcular_preco_final():.2f}")
print(f"Bombons com novo imposto: R$ {bombons.calcular_preco_final():.2f}")
