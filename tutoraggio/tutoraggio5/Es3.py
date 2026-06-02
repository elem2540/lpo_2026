class CFlightData:
    def __init__(self, ticket_code, flight_code, seat_num):
        self._ticket_code = ticket_code
        self._flight_code = flight_code
        self.seat_num = seat_num

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
            raise TypeError("Errore: il tipo di dato inserito non è consentito!")
        if new_seat < 0 or new_seat > 100:
            raise ValueError("Errore: il numero deve essere compreso tra 0 e 100!")
        else:
            self._seat_num = new_seat


class CListFlghtDataList:
    def __init__(self):
        self._lista = []

    def add_flight(self, ticket_code, flight_code, seat_num):
        if ticket_code is None:
            ticket_code = int(input("Inserisci numero biglietto: "))
        if flight_code is None:
            flight_code = int(input("Inserisci il codice del volo: "))
        if seat_num is None:
            seat_num = int(input("Inserisci il numero del posto: "))

        try:
            flight = CFlightData(ticket_code, flight_code, seat_num)
            self._lista = self._lista + [flight]
        except ValueError:
            print("Errore: il numero deve essere compreso tra 0 e 100!")
            self.add_flight(ticket_code, flight_code)
        except TypeError:
            print("Errore: il tipo di dato inserito non è consentito!")
            self.add_flight(ticket_code, flight_code)


if __name__ == "__main__":
    flight = CFlightData(123, 456, 150)
