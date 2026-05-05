from collections.abc import Iterator


class CIteratoreBatch(Iterator):
    def __init__(self, lista, batch_size):
        self.lista = lista
        self.batch_size = batch_size
        self.idx_current = 0

    def __next__(self):
        if self.idx_current + self.batch_size <= len(self.lista):
            elem = self.lista[self.idx_current:self.idx_current+self.batch_size]
            self.idx_current += self.batch_size
            return elem
        else:
            elem = self.lista[self.idx_current:]+self.lista[:(self.batch_size-(len(self.lista)-self.idx_current))]
            #Dario questa è una delle righe più belle/orribili che io abbia mai visto, complimenti
            self.idx_current = self.batch_size-(len(self.lista)-self.idx_current)
            return elem


l = [1, 2, 3, 4, 5]
oggetto_iteratore = CIteratoreBatch(l, 2)
n_iter = 4
for i in range(n_iter):
    print(next(oggetto_iteratore))
