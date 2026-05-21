import matplotlib.pyplot as plt

reddito = [2400, 1850, 1900, 1750, 1500, 1550, 1100, 800, 500, 400, 450, 300]
grado_istruzione = [6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]

plt.figure()
ax = plt.subplot()
plt.scatter(grado_istruzione, reddito)

plt.title('Relazione tra reddito e grado di istruzione')
plt.xlabel('Grado di istruzione')
plt.ylabel('Reddito')

plt.xticks([1, 2, 3, 4, 5, 6])
plt.grid()

ax.set_axisbelow(True)  # fa si che la griglia venga mostrata dietro i punti
nomi_grado_istr = ["elementari", "medie", "superiori", "triennale", "magistrale", "dottorato"]

ax.set_xticklabels(nomi_grado_istr, rotation=45, ha="right")
plt.subplots_adjust(0.125, 0.2, 0.98, 0.95)

plt.savefig("grafico_reddito_istruzione.png")
plt.show()
plt.close()
