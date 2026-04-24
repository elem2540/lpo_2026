class CPrelievoInvalido(Exception):
    def __init__(self, message):
        super().__init__(message)


class CContoCorrente:
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale

    def preleva(self, importo):
        if importo > self.saldo:
            raise CPrelievoInvalido(f"Il prelievo richiesto non può essere "
                                    f"effettuato. Hai cercato di prelevare {importo-self.saldo} "
                                    f"euro più di quelli presenti sul tuo conto.")
        self.saldo -= importo


if __name__ == "__main__":
    conto = CContoCorrente(100)
    """
    try:
        conto.preleva(150)
    except CPrelievoInvalido as e:
        print(e)
    """

    conto.preleva(150)
