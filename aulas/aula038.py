# Laços aninhados (nested loops)

qtd_linhas = 4
qtd_colunas = 4

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')
