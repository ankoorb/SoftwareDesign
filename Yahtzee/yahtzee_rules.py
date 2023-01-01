from hand import Hand
from rules import Rule, SameValueRule


class Aces(SameValueRule):

    def __init__(self):
        super().__init__("Aces", 1)


class Twos(SameValueRule):

    def __init__(self):
        super().__init__("Twos", 2)


class Threes(SameValueRule):

    def __init__(self):
        super().__init__("Threes", 3)


class Fours(SameValueRule):

    def __init__(self):
        super().__init__("Fours", 1)


class Fives(SameValueRule):

    def __init__(self):
        super().__init__("Fives", 5)


class Sixes(SameValueRule):

    def __init__(self):
        super().__init__("Sixes", 6)


class ThreeOfAKind(Rule):

    def name(self):
        return "Three of a kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i + 1) >= 3:
                return hand.sum()
        return 0


class FourOfAKind(Rule):

    def name(self):
        return "Four of a kind"

    def points(self, hand: Hand):
        for i in range(6):
            if hand.count(i + 1) >= 4:
                return hand.sum()
        return 0


class FullHouse(Rule):

    def name(self):
        return "Full House"

    def points(self, hand: Hand):
        counts = [hand.count(i + 1) for i in range(6)]
        if 2 in counts and 3 in counts:
            return 25
        return 0


class Straight(Rule):

    def is_straight(self, _list):
        if len(list(set(_list))) != len(_list):  # Verify no duplicates
            return False

        # Sum of n consecutive numbers: 1...n = n * (n+1) / 2
        consecutive_sum = (min(_list) + max(_list)) * (max(_list) - min(_list) + 1) / 2
        return sum(_list) == consecutive_sum


class SmallStraight(Straight):

    def name(self):
        return "Small Straight"

    def points(self, hand: Hand):
        _list = hand.get_hand()
        _list.sort()

        if len(_list) == 4 and self.is_straight(_list):
            return 30
        elif len(_list) == 5 and (self.is_straight(_list[1:]) or self.is_straight(_list[:-1])):
            return 30
        else:
            return 0


class LargeStraight(Straight):

    def name(self):
        return "Large Straight"

    def points(self, hand: Hand):
        if self.is_straight(hand.get_hand()):
            return 40
        return 0


class Yahtzee(Rule):

    def name(self):
        return "Yahtzee"

    def points(self, hand: Hand):
        if len(set(hand.get_hand())) == 1:
            return 50
        return 0


class FibonYahtzee(Rule):

    def name(self):
        return "FibonYahtzee"

    def points(self, hand: Hand):
        if sorted(hand.get_hand()) == [1, 1, 2, 3, 5]:
            return 100
        return 0


class Chance(Rule):

    def name(self):
        return "Chance"

    def points(self, hand: Hand):
        return hand.sum()
