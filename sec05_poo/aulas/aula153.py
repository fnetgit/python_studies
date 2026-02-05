# Método especial __call__

# Callable é algo que pode ser executado com parênteses
# O __call__ é invocado quando você chama a instância diretamente: obj(arg)
# Em classes normais, __call__ faz a instância de uma
# classe "callable".


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')
retorno = call1('Fco Neto')
# 1 Python vê call1('Fco Neto')
# 2  Detecta que call1 tem método __call__
# 3 AUTOMATICAMENTE executa: call1.__call__('Fco Neto')
# 4 Dentro __call__:
#    print('Fco Neto está chamando 23945876545')
#    return 2134
# 5 2134 é atribuído a variável 'retorno'


print(retorno)


call2 = CallMe('987654321')
call2('teste')
