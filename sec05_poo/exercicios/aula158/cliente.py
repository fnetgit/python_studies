import pessoa
import contas


class Cliente(pessoa.Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == "__main__":
    c1 = Cliente("Fco", 20)
    print(c1)
    c1.conta = contas.ContaPoupanca(111, 222, 0)
    print(c1.conta)

    c2 = Cliente("Mel", 19)
    print(c2)
    c2.conta = contas.ContaCorrente(111, 333, 0, 500)
    print(c2.conta)
