from collections.abc import Iterator


class CIterator(Iterator):
    def __init__(self, lista):
        self._lista = lista
        self.idx = 0

    def __next__(self):
        if self.idx < len(self._lista)-1:
            element = self._lista[self.idx]
            self.idx += 2
            return element
        else:
            raise StopIteration


if __name__ == "__main__":
    e_iter = CIterator([0, 1, 2, 3, 4, 5, 6])
    for i in e_iter:
        print(i)
