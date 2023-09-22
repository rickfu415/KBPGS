"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""



class Player():
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.mid_range_shoot = 0.4
        self.three_pointer = 0.2
        self.layup = 0.5
        self.total_points = 0