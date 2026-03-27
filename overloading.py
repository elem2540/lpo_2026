from functools import singledispatchmethod


class CFormattatore:
    @singledispatchmethod
    def formatta(self, dato):
        print("Dato non formattabile")

    @formatta.register
    def _(self, dato: list):
        print("Gli elementi della lista sono: ")
        for i in dato:
            print(i)

    @formatta.register
    def _(self, dato: dict):
        print("Gli elementi del dizionario sono: ")
        for chiave in dato:
            print(chiave, " = ",  dato[chiave])


formattatore = CFormattatore()
formattatore.formatta([1, 2, 3,])
formattatore.formatta({"a": 1, "b": 2})
