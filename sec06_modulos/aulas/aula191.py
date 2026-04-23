# requests para requisições HTTP

# obs.: aula190 era apenas testes dos comandos da aula189
# request é bib de terceiros
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response)  # código de status HTTP
print(response.status_code)
# print(response.headers)
# print(response.content) # formato de bytes
print(response.text)  # resposta em formato de string, geralmente JSON
