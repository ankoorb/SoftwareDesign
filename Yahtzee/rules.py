from hand import Hand
from abc import abstractmethod, ABC


class Rule(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def points(self, hand: Hand):
        pass


class SameValueRule(Rule):  # subclass to cover duplications

    def __init__(self, name: str, value: int):
        self.__name = name
        self.__value = value

    def name(self):
        return self.__name

    def points(self, hand: Hand):
        return hand.count(self.__value) * self.__value
