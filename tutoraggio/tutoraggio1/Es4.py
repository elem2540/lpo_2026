class CProduct:
    def __init__(self, id, price):
        self.id = id
        self.price = price


id = int(input("Inserisci id prodotto: "))
price = float(input("Inserisci prezzo prodotto: "))

prodotto = CProduct(id, price)

print("id: ", prodotto.id, "price: ", prodotto.price)