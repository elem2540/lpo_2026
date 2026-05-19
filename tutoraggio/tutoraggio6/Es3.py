import re

IBAN = r"[A-Z]{2}[0-9]{2}([A-Z]{1})([0-9]{5})([0-9]{5})([0-9]{12})"
IBAN_da_cercare = "IT70A1234512345000012345678"

iban = re.match(IBAN, IBAN_da_cercare).groups()

print("IBAN: ", iban)
print("CAB: ", iban[0])
print("ABI: ", iban[1])
print("CIN: ", iban[2])
