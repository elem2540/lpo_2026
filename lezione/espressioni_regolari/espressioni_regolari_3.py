import re

stringa_da_cercare = input("Inserire la stringa da verificare: ")
stringa = r"([a-z.-]+)@([a-z]+)\.([a-z]+)$"

match_obj = re.match(stringa, stringa_da_cercare)

if match_obj is not None:
    dominio = match_obj.groups()[1]
    print(dominio)
else:
    print("La stringa non è valida.")