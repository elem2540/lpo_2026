from abc import ABC, abstractmethod


class CProdotto:
    def __init__(self, codice_prodotto, prezzo, anno_vendita, anni_garanzia):
        self._codice_prodotto = codice_prodotto
        self._prezzo = prezzo
        self._anno_vendita = anno_vendita
        self._anni_garanzia = anni_garanzia

    @abstractmethod
    def calcola_garanzia(self):
        pass

    def calcola_prezzo_finale(self):
        return self._prezzo + self.calcola_garanzia()


class CElettronica(CProdotto):
    def __init__(self, codice_prodotto, prezzo, anno_vendita, anni_garanzia):
        super().__init__(codice_prodotto, prezzo, anno_vendita, anni_garanzia)

    def calcola_garanzia(self):
        if self._anni_garanzia == 4:
            return 500


class CElettrodomestici(CProdotto):
    def __init__(self, codice_prodotto, prezzo, anno_vendita, anni_garanzia):
        super().__init__(codice_prodotto, prezzo, anno_vendita, anni_garanzia)

    def calcola_garanzia(self):
        if self._anni_garanzia == 3:
            return 250
        if self._anni_garanzia == 5:
            return 400


telefono = CElettronica(123, 10, 2026, 4)
computer = CElettronica(789, 15, 2026, 4)
frigorifero = CElettrodomestici(456, 20, 2026, 5)
lavastoviglie = CElettrodomestici(321, 25, 2026, 3)

with open("sales.txt", "a") as file:
    for prodotto in [telefono, computer, frigorifero, lavastoviglie]:
        file.write("[{}| {}] Base: EURO {} - Garanzia: {} anni (+{} EURO) - Totale: {} EURO".format(
            prodotto._codice_prodotto, prodotto._anno_vendita,
            prodotto._prezzo, prodotto._anni_garanzia, prodotto.calcola_garanzia(),
            prodotto.calcola_prezzo_finale()))
        file.write("\n")
