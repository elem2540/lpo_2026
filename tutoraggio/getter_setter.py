class CStringa:
    def __init__(self,stringa):
        self._stringa = stringa
        self._lunghezza_stringa = self._calcola_lunghezza_stringa()

    def _calcola_lunghezza_stringa(self):
        len_stringa = len(self._stringa)
        return len_stringa

    @property
    def stringa(self):
        return self._stringa

    @stringa.setter
    def stringa(self, nuova_stringa):
        self._stringa = nuova_stringa
        self._lunghezza_stringa = self._calcola_lunghezza_stringa()

    @property
    def lunghezza_stringa(self):
        return self._lunghezza_stringa


# Esempio di utilizzo
stringa = CStringa("Hello World!")
print(f"Stringa: {stringa.stringa}")
print(f"Lunghezza della stringa: {stringa.lunghezza_stringa}")

