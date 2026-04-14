class CSensoreTemperatura:

    def __init__(self, numero_serie, temperatura):
        self._numero_serie = self._controllo_numero_serie(numero_serie)
        self._temperatura = self._controllo_temperatura(temperatura)

    @property
    def numero_serie(self):
        return self._numero_serie

    def _controllo_numero_serie(self, numero_serie):
        while numero_serie <= 0:
            print("Il numero di serie deve essere un numero positivo.")
            numero_serie = int(input("Inserisci un numero di serie valido: "))
        return numero_serie

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, nuova_temperatura):
        while nuova_temperatura < -100 or nuova_temperatura > 100:
            print("La temperatura deve essere compresa tra -100 e 100 gradi Celsius.")
            nuova_temperatura = float(input("Inserisci una temperatura valida: "))
        self._temperatura = nuova_temperatura

    def _controllo_temperatura(self,temperatura):
        while temperatura < -100 or temperatura > 100:
            print("La temperatura deve essere compresa tra -100 e 100 gradi Celsius.")
            temperatura = float(input("Inserisci una temperatura valida: "))
        return temperatura


# Esempio di utilizzo
sensore = CSensoreTemperatura(-123, -101)
print(f"Numero di serie:", sensore.numero_serie)
print(f"Temperatura: {sensore.temperatura} °C")