# asdict e astuple em dataclasses

from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if "__main__" == __name__:
    p1 = Pessoa("Fco", "N")
    print(asdict(p1))
    print(astuple(p1))
