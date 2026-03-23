# os e shutil - manipulação de arquivos e pastas

import os
from pathlib import Path
import shutil

HOME = os.path.expanduser("~")
print(HOME)

# caminho_2 = os.path.join("sec06_modulos", "2")
# caminho_aulas_2 = os.path.join("sec06_modulos", "aulas", "2")
# arquivo_teste = os.path.join(caminho_2, "arquivo.txt")

# os.makedirs(caminho_2, exist_ok=True)
# with open(arquivo_teste, "w") as f:
#     f.write("oi")

# shutil.copy(arquivo_teste, "sec06_modulos/arquivo_copiado.txt")

# shutil.copytree(caminho_2, "sec06_modulos/2_backup", dirs_exist_ok=True)

# os.makedirs("sec06_modulos/aulas", exist_ok=True)
# shutil.move(caminho_2, caminho_aulas_2)

# shutil.rmtree(caminho_aulas_2)

# Com pathlib
BASE_DIR = Path.home() / "Documents" / "cursos" / "python_studies" / "sec06_modulos"
pasta_2 = BASE_DIR / "2"
pasta_aulas_2 = BASE_DIR / "aulas" / "2"
pasta_backup = BASE_DIR / "2_backup"

pasta_2.mkdir(parents=True, exist_ok=True)
arquivo = pasta_2 / "teste.txt"
arquivo.write_text("exemplo")

shutil.copy(arquivo, BASE_DIR / "teste_copiado.txt")
shutil.copytree(pasta_2, pasta_backup, dirs_exist_ok=True)

(BASE_DIR / "aulas").mkdir(exist_ok=True)
shutil.move(pasta_2, pasta_aulas_2)

if pasta_aulas_2.exists():
    shutil.rmtree(pasta_aulas_2)

if pasta_backup.exists():
    shutil.rmtree(pasta_backup)

arquivo_copiado = BASE_DIR / "teste_copiado.txt"
if arquivo_copiado.exists():
    arquivo_copiado.unlink()
