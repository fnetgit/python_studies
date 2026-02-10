# Configurações em dataclasses

from dataclasses import dataclass


@dataclass(init=False)  # desativa a geração automática do __init__
# pode-se usar frozen=True para tornar a classe imutável

class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__post_init__()  # chamando manualmente

    # O método __post_init__ é chamado automaticamente após o __init__ gerado pela dataclass
    # como o __init__ foi desativado, o __post_init__ não será chamado automaticamente,
    # mas podemos chamá-lo manualmente dentro do __init__
    def __post_init__(self):
        print("POST INIT")


if __name__ == "__main__":
    p1 = Pessoa("Fco", "N")
    print(p1)
