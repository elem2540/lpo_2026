n = int(input("Quanti prodotti sono stati acquistati? "))
prodotti = []
tot = 0

if __name__ == "__main__":
    for prod in range(n):
        prezzo = float(input("Inserisci il prezzo: "))
        prodotti = prodotti + [prezzo]

        tot = tot + prezzo
        if tot > 100:
            tot = (tot*100)/5

    print("Il prezzo totale è:", tot)
