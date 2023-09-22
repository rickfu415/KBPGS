"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""
import player


class Team():
    def __init__(self, Name, ID):
        self.Name = Name
        self.ID = ID
        self.status = "None" # either in Offense or Defense
        self.current_score = 0
        