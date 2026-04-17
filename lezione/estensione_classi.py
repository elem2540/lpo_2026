class CListaElementi(list):
    def append(self, elemento):
        if elemento not in self:
            super().append(elemento)
        else:
            print("Elemento già presente: ", elemento)


if __name__ == "__main__":
    lista = CListaElementi()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    print(lista)
    lista.append(2)

