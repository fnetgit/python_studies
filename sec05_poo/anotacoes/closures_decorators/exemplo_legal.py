import time
import json
from urllib.request import urlopen


def calcular_tempo_execucao(func):
    def wrapper(url_alvo):
        inicio = time.time()
        hora_inicio = time.strftime('%H:%M:%S', time.localtime(inicio))

        print(f"Iniciando a requisição às {hora_inicio}.")

        try:
            resultado = func(url_alvo)
        except Exception as erro:
            print(f"Deu ruim: {erro}")
            resultado = None

        fim = time.time()
        hora_fim = time.strftime('%H:%M:%S', time.localtime(fim))
        print(f"Requisição finalizada em {hora_fim}.")
        print(f"Tempo de execução: {fim - inicio:.4f}s")
        return resultado
    return wrapper


@calcular_tempo_execucao
def obter_cotacao(url):
    with urlopen(url, timeout=5) as resposta:
        return json.loads(resposta.read())


dados = obter_cotacao("https://economia.awesomeapi.com.br/last/USD-BRL")

if dados:
    print(f"Dólar: R$ {dados['USDBRL']['bid']}")
