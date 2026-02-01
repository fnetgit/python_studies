# Abtração

# Uma classe abstrata é uma classe que não deve ser instanciada diretamente.
class Log:
    def _log(self, msg):  # assinatura do método
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    # log = Log() # Vai gerar um erro, pois não podemos instanciar uma classe abstrata
    # log.log('Olá Mundo')

    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('que legal')
