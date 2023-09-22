"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""
import team


class Game():
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.status = "None"
        self.round = 0 # either offense or offense is +1
        self.homeTeam = None
        self.guestTeam = None
