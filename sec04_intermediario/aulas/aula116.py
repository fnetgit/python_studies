import os

# Criando arquivos com Python + Context Manager with

# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita, apaga o que já existe), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (aceita iterável, concatena as strings)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'sec04_intermediario/aulas/aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open já abre e fecha o arquivo
with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:  # w+ = leitura e escrita
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n', 'Linha 5\n')
    )

    arquivo.seek(0, 0)
    print(arquivo.read())

print('#' * 20)

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())

os.rename(caminho_arquivo, 'sec04_intermediario/aulas/aula116_renomeado.txt')
os.remove(caminho_arquivo.replace('aula116', 'aula116_renomeado'))
