import re

stringa_data = "idx_[A-Z0-9]*$"
stringa_da_cercare = input("Inserire la stringa da verificare: ")

if len(stringa_da_cercare) > 4:
    print(re.match(stringa_data, stringa_da_cercare))
else:
    print("La stringa deve contenere almeno 5 caratteri.")
