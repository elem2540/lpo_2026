from math import pi
from abc import ABC, abstractmethod


class CFormaGeometrica(ABC):
    @abstractmethod
    def calcola_area(self):
        pass

    @abstractmethod
    def calcola_perimetro(self):
        pass


class CCerchio(CFormaGeometrica):

    def __init__(self):
        self.raggio = float(input("Inserisci il raggio del cerchio: "))

    def calcola_area(self):
        return pi * (self.raggio ** 2)

    def calcola_perimetro(self):
        return 2 * pi * self.raggio


class CRettangolo(CFormaGeometrica):
    def __init__(self):
        self.larghezza = float(input("Inserisci la larghezza del rettangolo:  "))
        self.altezza = float(input("Inserisci l'altezza del rettangolo:  "))

    def calcola_area(self):
        return self.larghezza * self.altezza

    def calcola_perimetro(self):
        return self.larghezza * 2 + self.altezza * 2


if __name__ == "__main__":
    forma = input("Vuoi calcolare area e perimetro di un cerchio (premi 0) o di un rettangolo (premi 1)? ")
    if forma == "0":
        cerchio = CCerchio()
        print("Area cerchio:", cerchio.calcola_area())
        print("Perimetro cerchio:", cerchio.calcola_perimetro())
    elif forma == "1":
        rettangolo = CRettangolo()
        print("Area rettangolo:", rettangolo.calcola_area())
        print("Perimetro rettangolo:", rettangolo.calcola_perimetro())
