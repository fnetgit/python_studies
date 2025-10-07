# Ambientes virtuais em Python (venv)

""" Um ambiente virtual cria uma pasta isolada que usa o Python principal do 
seu sistema como base, mas instala todas as bibliotecas de forma independente.

Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.

venv é o módulo que vamos usar para
criar ambientes virtuais.

Você pode dar o nome que preferir para um
ambiente virtual, mas os mais comuns são:
venv env .venv .env """


# Como criar ambientes virtuais

# python3 -m venv venv


# para saber o caminho do interpretador python
# which python3


# Ativando e desativando o ambiente virtual

# source venv/bin/activate
# deactivate


# Instalando pacotes no ambiente virtual
# pip install nome_do_pacote

# pip freeze - lista os pacotes instalados com suas versões (lembre de estar com o ambiente virtual ativado)
# pip freeze > requirements.txt - salva os pacotes instalados com suas versões no requirements.txt
# pip list - lista os pacotes instalados para uma boa visualização
# pip install -r requirements.txt - instala os pacotes listados no requirements.txt
# pip uninstall nome_do_pacote - desinstala o pacote especificado
