stringa = "Linguaggi di progrrammazione 33.8999"
stringa_pinga = stringa.split()

titolo = stringa_pinga[0] + " " + stringa_pinga[1] + " " + stringa_pinga[2]
prezzo = float(stringa_pinga[3])
print("{} {:.2f}".format(titolo, prezzo))
