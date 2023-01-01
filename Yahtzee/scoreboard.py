from hand import Hand
from rules import Rule
from typing import List


class ScoreBoard:

    def __init__(self):
        self.rules = []
        self.points = []

    # To use score board we want to be able to register rules
    def register_rules(self, rule: List):
        self.rules.extend(rule)
        # Reset points
        self.points = [0 for _ in range(len(self.rules))]

    @property
    def rule_count(self):
        return len(self.rules)

    def get_rule(self, idx: int):
        return self.rules[idx]

    def assign_points(self, rule: Rule, hand: Hand):
        idx = self.rules.index(rule)
        if self.points[idx] > 0:  # Check if points are already assigned
            raise Exception("Score Board already saved")
        points = rule.points(hand)
        self.points[idx] = points
        return points

    def total_points(self):
        return sum(self.points)

    def get_points_overview(self, hand: Hand = None):
        text = []
        for idx, rule in enumerate(self.rules):
            points = self.points[idx]
            if hand is not None and points == 0 and rule.points(hand) > 0:
                text.append(f"{idx + 1}. {rule.name()}: +{rule.points(hand)} possible points")
            else:
                text.append(f"{idx + 1}. {rule.name()}: +{points} points")
        return "\n".join(text)
