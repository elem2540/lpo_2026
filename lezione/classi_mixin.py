class CContaElementiMixin:
    def conta_elementi(self):
        num_elem = 0
        for elem in self.lista_elementi:
            num_elem += 1
        return num_elem


class CAnalisiDuplicatiMixin:
    def conta_duplicati(self):
        num_dup = 0
        for elem in self.lista_elementi:
            if self.lista_elementi.count(elem) > 1:
                num_dup += 1
        return num_dup

    def cerca_duplicati(self):
        duplicati = []
        for elem in self.lista_elementi:
            if self.lista_elementi.count(elem) > 1 and elem not in duplicati:
                duplicati.append(elem)
        return duplicati


class CStringa(CContaElementiMixin, CAnalisiDuplicatiMixin):
    def __init__(self, stringa):
        self.lista_elementi = stringa


class CLista(CContaElementiMixin, CAnalisiDuplicatiMixin):
    def __init__(self, lista):
        self.lista_elementi = lista


if __name__ == "__main__":

    ogg_stringa = CStringa("ciao a tutti")
    print("numero elementi nella stringa: ", ogg_stringa.conta_elementi())
    print("numero duplicati nella stringa: ", ogg_stringa.conta_duplicati())
    print("gli elementi duplicati sono: ", ogg_stringa.cerca_duplicati())

    ogg_lista = CLista([1, 2, 3, 4, 5, 1, 2])
    print("numero elementi nella lista:  ", ogg_lista.conta_elementi())
    print("numero duplicati nella lista: ", ogg_lista.conta_duplicati())
    print("gli elementi duplicati sono: ", ogg_lista.cerca_duplicati())
