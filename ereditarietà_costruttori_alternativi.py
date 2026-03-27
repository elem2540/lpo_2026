class CPersona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


class CStudente (CPersona):
    def __init__(self, nome, cognome, matricola, anno_di_nascita, classe_frequentata):
        super().__init__(nome, cognome)
        self.matricola = matricola
        self.anno_di_nascita = anno_di_nascita
        self.classe_frequentata = classe_frequentata

    @classmethod
    def crea_oggetto_studente(cls):
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        matricola = input("Inserisci il numero di matricola: ")
        anno_di_nascita = input("Inserisci l'anno di nascita: ")
        classe_frequentata = input("Inserisci la classe frequentata: ")
        return cls(nome, cognome, matricola, anno_di_nascita, classe_frequentata)

    def stampa_dati(self):
        print(self.nome, self.cognome, self.matricola, self.anno_di_nascita, self.classe_frequentata)


class CDocente (CPersona):
    def __init__(self, nome, cognome, materia_insegnata):
        super().__init__(nome, cognome)
        self.materia_insegnata = materia_insegnata

    @classmethod
    def crea_oggetto_docente(cls):
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        materia_insegnata = input("Inserire la materia insegnata: ")
        return cls(nome, cognome, materia_insegnata)

    def stampa_dati(self):
        print(self.nome, self.cognome, self.materia_insegnata)


class CAnagrafica:
    def __init__(self):
        self._persone = {}
        """self._persone = []"""

    def aggiungi_persona(self):
        scelta = int(input("Vuoi inserire uno studente (premi 0) o un docente (premi 1)? "))
        if scelta == 0:
            persona = CStudente.crea_oggetto_studente()
            self._persone[persona.nome] = persona
        else:
            if scelta == 1:
                persona = CDocente.crea_oggetto_docente()
                self._persone[persona.nome] = persona
            else:
                print("Scelta non disponibile!")

    def cerca_persona(self):
        nome = input("Inserisci il nome della persona da cercare: ")
        self._persone[nome].stampa_dati()

    """"
    def cerca_persona(self):
        nome = input("Inserisci il nome della persona da cercare: ")
        cognome = input("Inserisci il cognome della persona da cercare: ")
        i = 0
        while i < len(self._persone):
            persona = self._persone[i]
                if persona.nome == nome and persona.cognome == cognome:
                    self.persone[i].stampa_dati()
            i += 1
    """


anagrafica = CAnagrafica()
anagrafica.aggiungi_persona()
anagrafica.aggiungi_persona()

anagrafica.cerca_persona()
