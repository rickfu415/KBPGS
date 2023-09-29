"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""
import team


class Game():
    def __init__(self, rule, ID):
        self.rule = rule
        self.ID = ID
        self.status = "None"
        self.round = 0 # 1 offense + 1 defense is 1 round
        self.homeTeam = None
        self.guestTeam = None
