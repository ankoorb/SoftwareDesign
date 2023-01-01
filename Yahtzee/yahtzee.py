import os
import re
from hand import Hand
from scoreboard import ScoreBoard
from yahtzee_rules import (Aces, Twos, Threes, Fours, Fives, Sixes, ThreeOfAKind, FourOfAKind,
                           FullHouse, SmallStraight, LargeStraight, Yahtzee, FibonYahtzee, Chance)


class Game:

    def __init__(self):
        os.system("clear")
        message = """
        YAHTZEE
        
        Welcome to the game. To begin, simply press [Enter/Return] and follow the instructions
        on the screen.
        
        To exit, press [Ctrl + C]
        """
        print(message)

        # Instantiate hand and scoreboard
        self.hand = Hand()
        self.scoreboard = ScoreBoard()

        # Register rules for Yahtzee game
        self.scoreboard.register_rules([
            Aces(),
            Twos(),
            Threes(),
            Fours(),
            Fives(),
            Sixes(),
            ThreeOfAKind(),
            FourOfAKind(),
            FullHouse(),
            SmallStraight(),
            LargeStraight(),
            Yahtzee(),
            FibonYahtzee(),
            Chance(),
        ])

    def choose_dice_for_reroll(self):
        while True:
            try:
                reroll = input("\nChoose which dice to re-roll (comma-separated or 'all', or 0 to continue: ")
                if reroll.lower() == "all":
                    return self.hand.all_dice()
                else:
                    reroll = reroll.replace(" ", "")
                    reroll = re.sub(r"[^\d,]", "", reroll)
                    reroll = reroll.split(',')
                    reroll = list(map(int, reroll))

                if not reroll or 0 in reroll:
                    return []
                return reroll
            except ValueError:
                print("You have entered something other than a number.\nPlease try again.")
            except IndexError as ie:
                print(ie)

    def show_scoreboard_points(self, hand: Hand = None):
        print("\n SCORE BOARD")
        print("----------" * 4)
        print(self.scoreboard.get_points_overview(hand))
        print("----------" * 4)

    def select_scoring(self):
        self.show_scoreboard_points(self.hand)
        while True:
            idx = input("Choose which scoring rule to use: ")
            try:
                idx = int(re.sub(r"[^\d,]", "", idx))
                if idx < 1 or idx > self.scoreboard.rule_count:
                    print("Please select an existing scoring rule.")
                else:
                    return self.scoreboard.get_rule(idx - 1)
            except ValueError:
                print("You have entered something other than a number. Please try again.")

    def play_turn(self):
        rolls = 0
        selected_dice = self.hand.all_dice()  # Roll all dice
        while True:
            print("\nRolling dice...")
            self.hand.roll(selected_dice)
            print(self.hand)
            rolls += 1

            # Done if max number of rolls completed
            if rolls >= 3:
                break

            # Choose which dice to re-roll
            selected_dice = self.choose_dice_for_reroll()
            if not selected_dice:
                break

        rule = self.select_scoring()
        points = self.scoreboard.assign_points(rule, self.hand)
        print(f"Adding {points} points to {rule.name()}")
        self.show_scoreboard_points()

        input("\nPress any key to continue")
        os.system("clear")

    def play(self):
        for _ in range(self.scoreboard.rule_count):
            self.play_turn()
        print("\nCongratulations! You have finished the game!\n")
        self.show_scoreboard_points()
        print(f"Total points: {self.scoreboard.total_points()}")

if __name__ == "__main__":
    try:
        game = Game()
        game.play()
    except KeyboardInterrupt:
        print("\nExiting...")
