import random


class Die:
    def __init__(self, face: int = None, sides: int = 6):
        self.sides = sides
        if face is not None:
            self.__face = face
        else:
            self.roll()

    def roll(self):
        self.__face = random.randint(1, self.sides)
        return self.__face

    def get_face(self):
        return self.__face

    def set_face(self, value):
        self.__face = value

    def __str__(self):
        return str(self.__face)
