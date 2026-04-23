# protocolo HTTP

# é um protocolo de comunicação entre cliente e servidor, utilizado para
# transferência de dados na web que funciona por reequisição e resposta

# a mensagem de requisição do cliente deve incluir dados como:
# - o método HTTP
#   - leitura (GET, HEAD, OPTIONS)
#   - escrita (POST, PUT, PATCH, DELETE)
# - o endereço do recurso
# - os cabecalhos
# - o corpo da mensagem (opcional)

# criar servirdor HTTP simples com Python:

# na pasta do proj
# python3 -m http.server 8080

# fora da pasta do proj
# python3 -m http.server -d /caminho/diretorio/ 8080
