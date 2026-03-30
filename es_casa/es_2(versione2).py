class CEsame:
    def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
        self.nome_esame = nome_esame
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def calcola_media(self):
        return (self.voto_primo_parziale + self.voto_secondo_parziale) // 2


class CListaEsami:
    def __init__(self):
        self._lista_esami = []

    def aggiungi_esame(self):
        nome_esame = input("Inserisci il nome dell'esame: ")
        voto_primo_parziale = float(input("Inserisci il voto del primo parziale: "))
        voto_secondo_parziale = float(input("Inserisci il voto del secondo parziale: "))
        nuovo_esame = CEsame(nome_esame, voto_primo_parziale, voto_secondo_parziale)
        self._lista_esami += [nuovo_esame]

    def stampa_media_voti(self):
        for esame in self._lista_esami:
            print(f"Esame: {esame.nome_esame} - Voti: {esame.calcola_media()}")


Registro = CListaEsami()
Registro.aggiungi_esame()
Registro.aggiungi_esame()
Registro.stampa_media_voti()
