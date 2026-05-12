from collections.abc import Iterator
from random import randint


class CIteratore(Iterator):
    def __init__(self, lista):
        self._lista = lista

    def __next__(self):
        idx = randint(0, len(self._lista)-1)
        return self._lista[idx]


if __name__ == "__main__":
    rand_iter = CIteratore([2, 3, 5, 7, 8, 9])
    print(next(rand_iter))
