# os + shutil - movendo e apagando arquivos e pastas

import os
import shutil
from pathlib import Path

# caminho_2 = os.path.join("sec06_modulos", "2")
# caminho_aulas_2 = os.path.join("sec06_modulos", "aulas", "2")

# os.makedirs("sec06_modulos/aulas", exist_ok=True)
# if os.path.exists(caminho_2):
#     shutil.move(caminho_2, caminho_aulas_2)

# if os.path.exists(caminho_aulas_2):
#     shutil.rmtree(caminho_aulas_2)


# Usando pathlib
BASE_DIR = Path.home() / "Documents" / "cursos" / "python_studies" / "sec06_modulos"
pasta_2 = BASE_DIR / "2"
pasta_aulas_2 = BASE_DIR / "aulas" / "2"
pasta_backup = BASE_DIR / "2_backup"
arquivo_copiado = BASE_DIR / "teste_copiado.txt"

(BASE_DIR / "aulas").mkdir(exist_ok=True)

if pasta_2.exists():
    shutil.move(str(pasta_2), str(pasta_aulas_2))

if pasta_aulas_2.exists():
    shutil.rmtree(pasta_aulas_2)
if pasta_backup.exists():
    shutil.rmtree(pasta_backup)
if arquivo_copiado.exists():
    arquivo_copiado.unlink()
