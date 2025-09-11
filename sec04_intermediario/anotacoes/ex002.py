from data import products

# Nível Intermediário (Combinando Conceitos)

""" 
1 - Capitalizar Nomes de Móveis:
Objetivo: Crie uma nova lista chamada furniture_uppercase. Ela deve conter o nome, em letras 
maiúsculas, apenas dos produtos que pertencem à categoria 'Móveis'.
"""

"""
2 - Desconto para Eletrônicos Caros (Mapeamento com Condicional):

Objetivo: Crie uma nova lista de dicionários chamada electronics_with_discount. Para cada produto, 
se ele for da categoria 'Eletrônicos' E o preço for maior que R$ 100, o novo dicionário deve ter 
um preço com 10% de desconto. Caso contrário, o produto deve ser uma cópia exata do original. 
"""


# 1
furniture_uppercase = [product['nome'].upper()
                       for product in products
                       if product['categoria'] == 'Móveis']

# 2
# {**dicionario_antigo, 'chave_para_mudar': novo_valor}

electronics_with_discount = [{**product, 'preco': round(product['preco'] * 0.9, 2)}
                             if product['categoria'] == "Eletrônicos" and product['preco'] > 100 else product
                             for product in products
                             ]
