class CUser:
    def __init__(self, username):
        self.username: str = self._controlla_username(username)

    def _controlla_username(self, username):
        if type(username) is not str:
            raise TypeError("Lo username deve essere una stringa")

        if len(username) < 3 or len(username) > 5:
            raise ValueError("Lo username deve essere compreso tra 3 e 5")
        return username


if __name__ == "__main__":
    user = CUser("aa")
    print(user.username)
