"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma você já conhece bastante.
"""
variavel_1 = 1


def soma1(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    """Soma x, y e opcionalmente z (ESTILO SPHINX/reST).

    Se z não for informado, soma apenas x + y.

    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número  
    :type y: int or float
    :param z: Terceiro número (opcional)
    :type z: int or float or None
    :return: Soma dos números informados
    :rtype: int or float
    """
    if z is None:
        return x + y
    return x + y + z


def soma2(x: int | float, y: int | float, z: int | float | None = None) -> int | float:
    """Soma x, y e opcionalmente z (ESTILO GOOGLE/NUMPY).

    Se z não for informado, soma apenas x + y.

    Args:
        x (int | float): Primeiro número
        y (int | float): Segundo número
        z (int | float | None, optional): Terceiro número. Defaults to None.

    Returns:
        int | float: Soma dos números informados
    """
    if z is None:
        return x + y
    return x + y + z


if __name__ == "__main__":
    print("soma1(1, 2)        =", soma1(1, 2))
    print("soma1(1, 2, 3)    =", soma1(1, 2, 3))
    print("soma2(1, 2)        =", soma2(1, 2))
    print("soma2(1, 2, 3)    =", soma2(1, 2, 3))

variavel_2 = 2
variavel_3 = 3
