tipi = int(input("Quanti tipi di prodotti hai acquistato?  "))

prodotto = {}
lista = []
tot = 0

for tipo in range(tipi):
    prodotto = {
        "id":  str(input("Inserisci l'identificativo: ")),
        "quantità": int(input("Inserisci quante confezioni hai acquistato: ")),
        "costo": float(input("Inserisci il costo di ogni confezione: "))
    }
    lista.append(prodotto)
    tot = tot + prodotto["quantità"] * prodotto["costo"]
    if tot > 100:
        tot = (tot*100)/5

print("Il prezzo totale è: ", tot)
