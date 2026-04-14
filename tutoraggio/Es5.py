class CPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def print_coordinates(self):
        print("x: ", self.x, "y: ", self.y)


x = float(input("Inserisci coordinata x: "))
y = float(input("Inserisci coordinata y: "))

punto = CPoint(x, y)
punto.print_coordinates()
punto.reset()
punto.print_coordinates()
