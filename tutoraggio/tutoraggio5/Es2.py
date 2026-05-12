class CListWrapper(list):
    def remove(self, occorrenza) -> int:
        elem_r = 0
        for elem in self:
            if elem == occorrenza:
                super().remove(occorrenza)
                elem_r += 1
        return elem_r


if __name__ == "__main__":
    lis = CListWrapper([1, 2, 3, 4, 2])
    print("La lista è: ", lis)
    rimossi = lis.remove(2)
    print("Elementi rimossi: ", rimossi)
    print("Lista senza occorrenza: ", lis)
