# @property + @setter - getter e setter no modo Pythônico

# getter - um método para obter um atributo
# setter - um método para definir um atributo
# property - um método que se comporta como um atributo. Define o getter(leitura) e o setter(escrita).

# Atributos que começam com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:
    def __init__(self, cor, cor_tampa=None):
        # O Python prioriza o descritor (property) sobre o atributo comum.
        # A atribuição abaixo invoca o método @cor.setter imediatamente,
        # garantindo que a validação seja executada na inicialização.
        self.cor = cor
        # Atributo público simples: não precisa de property se não há lógica
        self.cor_tampa = cor_tampa

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if not valor:
            raise ValueError("A cor não pode ser vazia.")
        print(f'LOG: Alterando cor para {valor}')
        self._cor = valor


try:
    caneta = Caneta('Azul')
    caneta.cor = ''
except ValueError as e:
    print(f'Erro esperado: {e}')

caneta.cor_tampa = 'Preta'
