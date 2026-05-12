class Exam:
    def __init__(self, name: str, mark: int) -> None:
        self._name = name
        self.mark = mark

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if type(value) is not int:
            try:
                value = int(value)
            except ValueError:
                raise TypeError("il voto deve essere un intero")

        if (value < 0) or (value > 30):
            raise ValueError("Il voto deve essere un valore compreso tra 0 e 30")

        self._mark = value


class ExamList:
    def __init__(self):
        self._lista_esami = []

    def add_exam(self, name: str = None, mark: int = None):
        if name is None:
            name = input("Inserisci il nome: ")
        if mark is None:
            mark = int(input("Inserisci il voto: "))

        try:
            esame = Exam(name, mark)
            self._lista_esami.append(esame)
        except TypeError:
            print("Il voto inserito non è un intero!")
            self.add_exam(name)
        except ValueError:
            print("Il voto inserito non è un numero valido!")
            self.add_exam(name)
