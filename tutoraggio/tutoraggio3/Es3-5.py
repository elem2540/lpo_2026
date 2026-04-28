class CUser:
    def __init__(self, tax_code, birth_year, postal_code):
        self._tax_code = tax_code
        self._birth_year = birth_year
        self._postal_code = postal_code

    @property
    def tax_code(self):
        return self._tax_code

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, new_postal):
        self._postal_code = new_postal


if __name__ == "__main__":
    user = CUser(12, 2004, "09013")
    user.postal_code = "09010"
    print("new postal code: ", user.postal_code)
