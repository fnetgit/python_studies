class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.nome!r}, {self.idade!r})"
        return f"{class_name}{attrs}"
