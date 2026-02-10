"""
Implementando Protocolos Iterator E Sequence

ITERATOR: __iter__() + __next__() → for item in obj:
SEQUENCE: __len__() + __getitem__() → len(obj), obj[0], obj[0:3]

collections.abc.Sequence = Iterator + Sequence + mais métodos
"""

from collections.abc import Sequence

# sequence auto adiciona __contains__, __iter__, __reversed__, index, count
from typing import Any


class MyList(Sequence[Any]):  # Herda ABC completo
    def __init__(self):
        self._data: dict[int, Any] = {}
        self._index = 0
        self._next_index = 0  # Para iterador

    def append(self, *values: Any) -> None:
        """Adiciona múltiplos valores (varargs)."""
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        """len(my_list) → tamanho."""
        return self._index

    def __getitem__(self, index: int | slice) -> Any:
        """my_list[0], my_list[1:3] → slicing incluso!"""
        if isinstance(index, slice):
            start, stop, step = index.indices(self._index)
            return [self._data[i] for i in range(start, stop, step)]
        return self._data[index]

    def __setitem__(self, index: int, value: Any) -> None:
        """my_list[0] = 'novo' (mutável)."""
        if index >= self._index:
            raise IndexError("Index fora do range")
        self._data[index] = value

    # ITERATOR (reset no __iter__)
    def __iter__(self):
        """for item in my_list: → itera do início."""
        self._next_index = 0  # Reset toda vez
        return self

    def __next__(self):
        """next(iterator) → próximo item."""
        if self._next_index >= self._index:
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value

    # herdado de Sequence, mas customizado
    def __contains__(self, item: Any) -> bool:
        return item in self._data.values()


if __name__ == "__main__":
    lista = MyList()
    lista.append("Fco", "N")
    lista[0] = "Mel"  # __setitem__
    lista.append("Duque")

    print("Lista completa:", lista[:])  # slicing
    print("Tamanho:", len(lista))
    print("Primeiro:", lista[0])

    print("\n1º LOOP:")
    for item in lista:  # Iterator reset
        print(item)

    print("\n2º LOOP:")
    for item in lista:
        print(item)

    print("\nin:", "Duque" in lista)  # __contains__
