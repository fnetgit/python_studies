# Ordene esses nomes em uma lista de strings ordenadas
# alfabeticamente com os números na frente.


nomes_str = "1. Willamy Josué Santos Serejo 2. Samuel da Penha Nascimento 3. Mariana da Mota Pinho 4. Vitor Dos Santos Correia 5. Mayara Lima Miranda 6. Ruan Pedro de Araujo Anjos 7. Jordan Fernandes de Carvalho 8. José Wilk Souza Lima 9. Francisco Alves Ribeiro Neto 10. Gabriel Lima Silva Oliveira 11. Ivanido dos Santos Araujo 12. Denis do Nascimento Rodrigues 13. Fabrício Fontenele Vieira 14. Alan Rodrigues de Castro 15. Paulo Henrique Alves Vieira 16. Victor Emanoel Lima Silva 17. Eric Silva Patricio 18. Francisco Osmar Santos Silva 19. Erick Vieira da Silva Costa 20. Gabriel Oliveira Pinto 21. Luis Felipe Ferreira Martins 22. Felipe Martins Dos Santos Silva 23. Enzo Damasceno Falcão 24. Kauã Neres Moura 25. Henrique Veras Cordeiro"


# lista_s_numeros = []
# for digito in nomes_str:
#     if not digito.isnumeric() is True:
#         lista_s_numeros.append(digito)
# string_final = "".join(lista_s_numeros)
# lista_de_nomes = string_final.split('. ')

# nomes_limpos = []
# for nome in lista_de_nomes:
#     if nome:
#         nomes_limpos.append(nome.strip())
# nomes_ordenados = sorted(nomes_limpos)

# for i, nome in enumerate(nomes_ordenados, 1):
#     print(f'{i}. {nome}')


nomes_s_num = [digito for digito in nomes_str if not digito.isnumeric()]
string_final = "".join(
    [digito for digito in nomes_str if not digito.isnumeric()])
lista_de_nomes = string_final.split('. ')
nomes_limpos = [nome.strip() for nome in lista_de_nomes if nome]
nomes_ordenados = sorted(nomes_limpos)
listar_nomes = [print(f'{i}. {nome}') for i, nome in enumerate(nomes_ordenados, 1)]



nomes_lista = ["1. Willamy Josué Santos Serejo",
               "2. Samuel da Penha Nascimento",
               "3. Mariana da Mota Pinho",
               "4. Vitor Dos Santos Correia",
               "5. Mayara Lima Miranda",
               "6. Ruan Pedro de Araujo Anjos",
               "7. Jordan Fernandes de Carvalho",
               "8. José Wilk Souza Lima",
               "9. Francisco Alves Ribeiro Neto",
               "10. Gabriel Lima Silva Oliveira",
               "11. Ivanido dos Santos Araujo",
               "12. Denis do Nascimento Rodrigues",
               "13. Fabrício Fontenele Vieira",
               "14. Alan Rodrigues de Castro",
               "15. Paulo Henrique Alves Vieira",
               "16. Victor Emanoel Lima Silva",
               "17. Eric Silva Patricio",
               "18. Francisco Osmar Santos Silva",
               "19. Erick Vieira da Silva Costa",
               "20. Gabriel Oliveira Pinto",
               "21. Luis Felipe Ferreira Martins",
               "22. Felipe Martins Dos Santos Silva",
               "23. Enzo Damasceno Falcão",
               "24. Kauã Neres Moura",
               "25. Henrique Veras Cordeiro"]

# sorted_names = []
# for i in nomes_lista:
#     sorted_names.append(i.split('. '))

# for i, name in enumerate(sorted_names):
#     sorted_names[i] = sorted_names[i][1]
# sorted_names.sort()

# for i, name in enumerate(sorted_names):
#     print(f'{i + 1}. {name}')

nomes_apenas = [item.split('. ')[1].strip() for item in nomes_lista]

nomes_apenas.sort()

for i, nome in enumerate(nomes_apenas, 1):
    print(f'{i}. {nome}')
