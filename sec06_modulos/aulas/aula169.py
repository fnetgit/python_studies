# os path - manipulação de caminhos de arquivos e diretórios

import os

file_path = os.path.join(
    "sec06_modulos", "aulas", "aula169.py"
)  # monta caminho relativo; resolvido a partir do cwd
print(file_path)

dire, file = os.path.split(file_path)  # faz uma tupla com o diretório e o arquivo
print("Diretório:", dire)
print("Arquivo:", file)

print(os.path.exists(file_path))

print(os.path.abspath("."))
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
