importo_tot = 0

with open("pagamenti_maggio.txt", "r") as pagamenti:
    righe = pagamenti.readlines()

    for riga in righe:
        codice, importo = riga.split()
        print(f"Codice fornitore: {codice} Importo: {importo}")
        importo_tot = importo_tot + int(importo)

print("L'importo totale è: ", importo_tot)
