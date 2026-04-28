class CFlightData:
    def __init__(self, ticket_code, flight_code, seat_num):
        self._ticket_code = ticket_code
        self._flight_code = flight_code
        self._seat_num = seat_num

    @property
    def ticket_code(self):
        return self._ticket_code

    @property
    def flight_code(self):
        return self._flight_code

    @property
    def seat_num(self):
        return self._seat_num

    @seat_num.setter
    def seat_num(self, new_seat):
        if type(new_seat) is int:
            self._seat_num = new_seat
        else:
            print("Errore: il tipo di dato inserito non è consentito!")
        if new_seat < 0 or new_seat > 100:
            print("Errore: il numero deve essere compreso tra 0 e 100")
        else:
            self._seat_num = new_seat


if __name__ == "__main__":
    flight = CFlightData(123, 456, 150)
