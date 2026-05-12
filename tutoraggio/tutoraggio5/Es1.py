class CListWrapper(list):
    def remove(self, occorrenza) -> None:
        for elem in self:
            if elem == occorrenza:
                super().remove(occorrenza)


if __name__ == "__main__":
    lis = CListWrapper([1, 2, 3, 4, 2])
    print(lis)
    lis.remove(2)
    print("Lista senza occorrenza: ", lis)
