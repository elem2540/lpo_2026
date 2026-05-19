from collections.abc import Iterator


class CIterator(Iterator):
    def __init__(self, lista):
        self._lista = lista
        self.idx = 0

    def __next__(self):
        if self.idx < len(self._lista):
            element = self._lista[self.idx]
            self.idx += 2
            return element
        else:
            raise StopIteration


class CNewEventList(list):
    def __iter__(self):
        return CIterator(self)


if __name__ == "__main__":
    ls = [0, 1, 2, 3, 4, 5, 6]
    new_list = CNewEventList(ls)
    for elem in new_list:
        print(elem)
