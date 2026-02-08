import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f"(DEPÓSITO {valor:.2f})")
        return self.saldo

    def detalhes(self, msg: str = "") -> None:
        print(f"O seu saldo é {self.saldo:.2f} {msg}")
        print("=-" * 20)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r}, {self.conta!r}, {self.saldo!r})"
        return f"{class_name}{attrs}"


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado")
        self.detalhes(f"(SAQUE {valor:.2f} NEGADO)")
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int, saldo: float = 0, limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self.saldo

        print("Não foi possível sacar o valor desejado")
        print(f"Seu limite é {-self.limite:.2f}")
        self.detalhes(f"(SAQUE {valor:.2f} NEGADO)")
        return self.saldo

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.limite!r})"


if __name__ == "__main__":
    cp1 = ContaPoupanca(1, 123456, 0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    cp1.detalhes()

    print("\n")

    cc1 = ContaCorrente(1, 123456, 0)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    cc1.detalhes()
