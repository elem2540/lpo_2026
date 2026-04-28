from random import randint


class CGhost:
    start_speed = 10
    speed = start_speed

    def __init__(self):
        self.pos_x, self.pos_y = self.generate_random_position()

    @staticmethod
    def generate_random_position():
        pos_x = randint(0, 100)
        pos_y = randint(0, 100)
        return pos_x, pos_y

    @classmethod
    def reset_speed(cls):
        cls.speed = cls.start_speed

    @classmethod
    def increase_speed(cls):
        cls.speed += 50


if __name__ == "__main__":
    ghost1 = CGhost()
    ghost2 = CGhost()

    print(ghost1.generate_random_position())
    print(ghost2.generate_random_position())

    print(ghost1.speed)
    print(ghost2.speed)

    ghost1.increase_speed()

    print(ghost1.speed)
    print(ghost2.speed)

    ghost2.reset_speed()

    print(ghost1.speed)
    print(ghost2.speed)
