import re

stringa_data = "https://lpo/slide_parte_[0-9]\.pdf"
stringa_da_cercare = input("Inserire la stringa da verificare: ")

print(re.match(stringa_data, stringa_da_cercare))
