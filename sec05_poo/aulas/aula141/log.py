# Abtração

# Uma classe abstrata é uma classe que não deve ser instanciada diretamente.

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):  # assinatura do método
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'salvando no log {msg_formatada}')
        with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('que legal')
