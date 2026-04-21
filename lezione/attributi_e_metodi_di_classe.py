class CProgrammatore:
    stipendio_base = 1500

    def __init__(self, nome, cognome) -> None:
        self.nome = nome
        self.cognome = cognome


class CProgrammatoreJunior(CProgrammatore):
    @classmethod
    def calcola_stipendio(cls, mese) -> int:
        if mese == 12:
            return cls.stipendio_base + 500
        else:
            return cls.stipendio_base


class CProgrammatoreSenior(CProgrammatore):
    @classmethod
    def calcola_stipendio(cls, mese) -> int:
        if mese == 12:
            return cls.stipendio_base + 1000
        else:
            return cls.stipendio_base


if __name__ == "__main__":
    print("Lo stipendio di un programmatore junior a dicembre è: ", CProgrammatoreJunior.calcola_stipendio(12))
    print("Lo stipendio di un programmatore senior a dicembre è: ", CProgrammatoreSenior.calcola_stipendio(12))
    print("Lo stipendio di un programmatore junior a luglio è: ", CProgrammatoreJunior.calcola_stipendio(7))
