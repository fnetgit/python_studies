# Classes abstratas - Abstract Base Class (ABC)

# Classes abstratas (ABCs) definem contratos para subclasses.
# Podem ter métodos abstratos (obrigatórios nas subclasses) e métodos concretos.

# Métodos marcados com @abstractmethod não têm implementação
# e tornam a classe abstrata (não pode ser instanciada diretamente).

# Uma ABC em Python usa ABCMeta como metaclasse (via ABC).
# É possível ter @property, @setter, @classmethod e @staticmethod
# abstratos; use @abstractmethod como decorador mais interno.

from abc import ABC, ABCMeta, abstractmethod


# class Log(metaclass=ABCMeta) é equivalente a class Log(ABC),
# pois ABC usa ABCMeta como metaclasse.


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Oi')
