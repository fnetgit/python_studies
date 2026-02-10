# Dataclasses

# Dataclasses auto-geram __init__, __repr__, __eq__ e mais, reduzindo código
# repetitivo para modelos de dados simples.

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


# sem dataclass:
class Pessoa2:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa2(nome={self.nome!r}, sobrenome={self.sobrenome!r}, idade={self.idade})"

    def __eq__(self, other):
        if not isinstance(other, Pessoa2):
            return NotImplemented
        return (self.nome, self.sobrenome, self.idade) == (
            other.nome,
            other.sobrenome,
            other.idade,
        )


if __name__ == "__main__":
    p1 = Pessoa("Fco", "N", 20)
    p2 = Pessoa("Fco", "N", 20)
    print(p1 == p2)
    print(p1)

    p3 = Pessoa2("Fco", "N", 20)
    p4 = Pessoa2("Fco", "N", 20)
    print(p3 == p4)
    print(p3)
