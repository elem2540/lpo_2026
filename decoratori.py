def class_method(funzione):
    def wrapper(*varargs, **kwargs):
        print("Applica la funzione", funzione.__name__, "passando come argomenti senza keyword: ", varargs,"e con keyword: ", kwargs)
        classe = type(varargs[0])
        funzione(classe, *varargs[1:], **kwargs)
    return wrapper


class CProva:
    val = 1000

    def __init__(self):
        self.val = 9999

    @class_method
    def stampa_val(cls):
        print(cls)
        print(cls.val)


prova = CProva()
prova.stampa_val() #stampa 1000 --> dimostrazione che sta usando l'attr di classe
print(prova.val)   #stampa 9999 --> dimostrazione che sta usando l'attr di istanza




