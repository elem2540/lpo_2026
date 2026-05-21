import matplotlib.pyplot as plt

vendite = [900, 1000, 600, 100, 100, 200, 400, 600, 800, 900, 1000, 1200]
mesi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.figure()
ax = plt.subplot()
plt.plot(mesi, vendite)

plt.title('Vendite del 2020')
plt.xlabel('Mese')
plt.ylabel('Numero di prodotti venduti')

plt.xticks(mesi)
plt.grid()

nomi_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio",
             "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

ax.set_xticklabels(nomi_mesi, rotation=45, ha="right")
plt.xlim(1, 12)
plt.subplots_adjust(0.125, 0.2, 0.98, 0.95)

plt.savefig("grafico_vendite.png")
plt.show()
plt.close()
