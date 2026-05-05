from abc import ABC, abstractmethod


class CExam(ABC):

    @abstractmethod
    def voto_finale(self):
        pass


class CWeightedPartialExam(CExam):
    def __init__(self, voto_primo_parziale, voto_secondo_parziale, peso_primo_parziale, peso_secondo_parziale):
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale
        self.peso_primo_parziale = peso_primo_parziale
        self.peso_secondo_parziale = peso_secondo_parziale

    def voto_finale(self):
        return (((self.voto_primo_parziale*self.peso_primo_parziale) +
                (self.voto_secondo_parziale*self.peso_secondo_parziale)) /
                (self.peso_primo_parziale+self.peso_secondo_parziale))


if __name__ == "__main__":
    esame = CWeightedPartialExam(28,30,0.5,0.5)
    print(esame.voto_finale())