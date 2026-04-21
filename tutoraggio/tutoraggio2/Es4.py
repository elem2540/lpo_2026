class CWordCounter:

    def __init__(self, lista: list[str]) -> None:
        self.lista = lista
        self._dizionario = {}

    def count(self) -> None:
        for word in self.lista:
            if word not in self._dizionario:
                self._dizionario[word] = 1
            else:
                self._dizionario[word] += 1

    def print_occurences(self) -> None:
        for key, value in self._dizionario.items():
            print(f"{key} -> {value}")


if __name__ == "__main__":
    lista = ["Python", "è", "un", "linguaggio", "di", "programmazione", "Python", "è", "molto", "popolare"]
    counter = CWordCounter(lista)
    counter.count()
    counter.print_occurences()
