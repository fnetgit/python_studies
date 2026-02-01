# Abtração

# Uma classe abstrata é uma classe que não deve ser instanciada diretamente.
class Log:
    def log(self, msg):  # assinatura do método
        raise NotImplementedError('Implemente o método log')


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    # log = Log() # Vai gerar um erro, pois não podemos instanciar uma classe abstrata
    # log.log('Olá Mundo')

    l = LogFileMixin()
    l.log('qualquer coisa')
