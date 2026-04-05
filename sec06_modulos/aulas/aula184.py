# Variáveis de ambiente

# no sistema operacional, podem ser criadas assim:
# terminal: export NOME_VAR=valor
# acesso: echo $NOME_VAR

import os
from dotenv import load_dotenv  # uv add python-dotenv

load_dotenv()
print(os.environ, "\n")  # dict com todas as variáveis de ambiente carregadas do .env

print(os.getenv("NOME_VAR"))
# tem que ser executado no mesmo terminal onde a variável foi criada
