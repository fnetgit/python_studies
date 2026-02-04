# Context Manager com classes - Criando e Usando gerenciadores de contexto

# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.

# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.

# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.

# Para criar um context manager, basta implementar:
# - __enter__(): chamado no início do bloco 'with'
# - __exit__(exc_type, exc_value, traceback): chamado no final (ou em erro)

# O método __exit__ recebe três argumentos sobre exceções:
# - class_exception: a classe da exceção (por exemplo, ValueError)
# - exception_: a instância da exceção
# - traceback_: o rastreamento da exceção

# Retorno do __exit__:
# - True: suprime a exceção
# - False/None: propaga a exceção


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, exc_type, exc_value, traceback):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        if exc_type is not None:
            print(f'Exceção capturada: {exc_type.__name__}: {exc_value}')

            # return True  # Suprime exceção
            return False  # Propaga exceção


# Teste sem exceção
print('Teste sem exceção:')
with MyOpen('sec05_poo/aulas/aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    print('WITH concluído')

print('\nTeste com exceção:')
try:
    with MyOpen('sec05_poo/aulas/aula149.txt', 'w') as arquivo:
        arquivo.write('Linha 1\n')
        arquivo.write('Linha 2\n', 123)  # Erro
except TypeError as e:
    print(f'Exceção propagada: {e}')
