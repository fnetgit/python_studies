# os e shutil - copiando arquivos e criando pastas

import os
from pathlib import Path
import shutil

print(os.path.expanduser("~"))

# caminho_2 = os.path.join("sec06_modulos", "2")
# arquivo_teste = os.path.join(caminho_2, "arquivo.txt")

# os.makedirs(caminho_2, exist_ok=True)
# with open(arquivo_teste, "w", encoding="utf-8") as f:
#     f.write("oi")

# shutil.copy(arquivo_teste, "sec06_modulos/arquivo_copiado.txt")
# shutil.copytree(caminho_2, "sec06_modulos/2_backup", dirs_exist_ok=True)


# Usando pathlib
BASE_DIR = Path.home() / "Documents" / "cursos" / "python_studies" / "sec06_modulos"
pasta_2 = BASE_DIR / "2"
pasta_backup = BASE_DIR / "2_backup"

pasta_2.mkdir(parents=True, exist_ok=True)
arquivo = pasta_2 / "teste.txt"
arquivo.write_text("exemplo")

shutil.copy(arquivo, BASE_DIR / "teste_copiado.txt")
shutil.copytree(pasta_2, pasta_backup, dirs_exist_ok=True)
