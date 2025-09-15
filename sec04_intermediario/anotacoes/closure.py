# closure

def criar_formatador_de_log(prefixo):

    def mensagem_recebida(mensagem):
        return prefixo + mensagem

    return mensagem_recebida


erro = criar_formatador_de_log('[ERRO]:')
informacao = criar_formatador_de_log('[INFO]:')

erro_de_leitura_no_disco = erro('leitura no disco')
informacao_de_temperatura_alta = informacao('temperatura alta')

print(erro_de_leitura_no_disco)
print(informacao_de_temperatura_alta)
