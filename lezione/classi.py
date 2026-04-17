class CEsame:
    def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
        self.nome_esame = nome_esame
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def calcola_media(self):
        return (self.voto_primo_parziale+self.voto_secondo_parziale)/2

    def stampa_voto_finale(self):
        print(f"Il voto finale è: {self.calcola_media()}")


class CListaVoti:
    def __init__(self):
        self._lista_esami = []

    def aggiungi_esame(self):
        nome_esame = input("Iserisci il nome dell'esame: ")
        voto_primo_parziale = float(input("Iserisci il voto del primo parziale: "))
        voto_secondo_parziale = float(input("Iserisci il voto del secondo parziale: "))

        nuovo_esame = CEsame(nome_esame, voto_primo_parziale, voto_secondo_parziale)
        self._lista_esami = self._lista_esami + [nuovo_esame]

    def mostra_nome_esame_voto_piu_alto(self):
        voto_max = self._lista_esami[0].calcola_media()
        for nome_esame in range(len(self._lista_esami)):
            if voto_max < self._lista_esami[nome_esame].calcola_media():
                voto_max = self._lista_esami[nome_esame].calcola_media()
        for i in range(len(self._lista_esami)):
            if self._lista_esami[i].calcola_media() == voto_max:
                print(self._lista_esami[i].nome_esame)


num = int(input("Quanti esami vuoi inserire? "))
i = 0
lista_voti = CListaVoti()

while i < num:
    print(f"Inserisci i dati dell'esame {i+1}: ")
    lista_voti.aggiungi_esame()
    i += 1

print("Esame/i con voto più alto:")
lista_voti.mostra_nome_esame_voto_piu_alto()
