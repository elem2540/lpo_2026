from math import pi
from math import sqrt


class CPoint:
    def __init__(self, x, y) -> None:
        self.x: float = x
        self.y: float = y

    def reset(self) -> None:
        self.x = 0
        self.y = 0

    def print_coordinates(self) -> None:
        print("x: ", self.x, "y: ", self.y)


class CCircle:
    def __init__(self, x: float, y: float, raggio: float) -> None:
        self.x: float = x
        self.y: float = y
        self.raggio: float = raggio

    def area(self) -> float:
        return pi * (self.raggio ** 2)

    def perimetro(self) -> float:
        return 2 * pi * self.raggio


class CSegment:
    def __init__(self, p1_x, p1_y, p2_x, p2_y) -> None:
        self.p1 = CPoint(p1_x, p1_y)
        self.p2 = CPoint(p2_x, p2_y)

    def calc_length(self) -> float:
        return sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)


if __name__ == "__main__":

    choice = input("Vuoi inserire un punto, un cerchio o un segmento? Digita 'punto', 'cerchio' o 'segmento':  ")

    if choice == 'punto':
        x = float(input("Inserisci coordinata x: "))
        y = float(input("Inserisci coordinata y: "))

        punto = CPoint(x, y)
        punto.print_coordinates()
        punto.reset()
        punto.print_coordinates()

    elif choice == 'cerchio':
        x = float(input("Inserisci coordinata x del centro: "))
        y = float(input("Inserisci coordinata y del centro: "))
        raggio = float(input("Inserisci raggio del cerchio: "))

        cerchio = CCircle(x, y, raggio)
        print("L'area del cerchio è: ", cerchio.area())
        print("Il perimetro del cerchio è: ", cerchio.perimetro())

    elif choice == 'segmento':
        segmento = CSegment(0, 0, 2, 2)
        print("La lunghezza del segmento è: ", segmento.calc_length())
