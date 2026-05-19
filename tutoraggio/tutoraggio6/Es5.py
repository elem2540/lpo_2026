lista = []

with open("passeggeri.txt", "r") as passeggeri:
    lines = passeggeri.readlines()

    for line in lines:
        nome, cognome, codice_posto_a_sedere = line.split()
        lista.append({"Nome: ": nome, "Cognome: ": cognome, "Codice posto a sedere: ": codice_posto_a_sedere})

for passeggero in lista:
    print(passeggero)
