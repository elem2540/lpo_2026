from math import log
import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []

for i in n:
    lista.append(log(i))

plt.plot(n, lista)
plt.grid()
plt.title("Grafico logaritmo")
plt.xlabel("n")
plt.ylabel("log(n)")
plt.show()
plt.close()