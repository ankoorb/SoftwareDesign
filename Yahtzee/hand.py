from die import Die


class Hand:

    def __init__(self, dice: int = 5, sides: int = 6):
        self.dice = dice
        self.hand = [Die(None, sides) for _ in range(self.dice)]

    def all_dice(self):
        return range(1, self.dice + 1)

    def roll(self, dice):
        # Check validity of dice list
        if [d for d in dice if d > self.dice or d < 1]:
            raise IndexError(f"You only have {self.dice} dice")

        for i in dice:
            self.hand[i-1].roll()  # i-1 because dice list is user input

    def get_hand(self):
        return [die.get_face() for die in self.hand]

    def set_faces(self, values):
        for idx, value in enumerate(values):
            self.hand[idx].set_face(value)

    def count(self, value):
        return self.get_hand().count(value)

    def sum(self):
        return sum(self.get_hand())

    def __str__(self):
        return "\n".join([f"die {idx + 1} has value {die}" for idx, die in enumerate(self.hand)])
