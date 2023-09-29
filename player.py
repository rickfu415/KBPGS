"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""

import random
import utility

class Player():
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.mid_range_shoot = 0.3
        self.three_pointer = 0.2
        self.layup = 0.3
        self.mistake_to_turnover = 0.1
        self.total_points = 0
        self.choice_probability = None # should be cumulative sections.
    
    def initialize(self):
        vec = [self.mid_range_shoot, self.three_pointer, self.layup]
        self.choice_probability = utility.weighted_sections(vec)

    def status_check(self):
        if (self.mid_range_shoot<0 or self.mid_range_shoot>1):
            print("Wrong probability for player",self.name)
            self.mid_range_shoot = int(self.mid_range_shoot)

        if (self.three_pointer<0 or self.three_pointer>1):
            print("Wrong probability for player",self.name)
            self.three_pointer = int(self.three_pointer)

        if (self.layup<0 or self.layup>1):
            print("Wrong probability for player",self.name)
            self.layup = int(self.layup)

    def show(self):
        print("Player name:",self.name, "ID:",self.ID,
              " Mid-range=",self.mid_range_shoot,
              " ThreePointer=",self.three_pointer,
              " Layup=",self.layup)
    
    def offense(self):
        result = 0
        # determine if mistake  leads to turn over
        if (random.uniform(0, 1) < self.mistake_to_turnover):
            print("--- ",self.name," missed and leads to turn over.")
            return -1

        # determine if mid-range, layup or three-pointer
        choice = utility.find_range(random.uniform(0, 1), self.choice_probability)
        if (choice==0):
            if (self.mid_range_shoot>random.uniform(0, 1)):
                self.total_points += 2
                print("--- ", self.name," made a mid-range shot.")
                return 2
            else:
                print("--- ", self.name," missed a mid-range shot.")
                return 0
        elif (choice==1):
            if (self.three_pointer>random.uniform(0, 1)):
                self.total_points += 3
                print("--- ", self.name," made a three_pointer shot.")
                return 3
            else:
                print("--- ", self.name," missed a three_pointer shot.")
                return 0
        elif (choice==2):
            if (self.layup>random.uniform(0, 1)):
                self.total_points += 2
                print("--- ", self.name," made a layup shot.")
                return 2
            else:
                print("--- ", self.name," missed a layup shot.")
                return 0

        return result



if __name__ == "__main__":
    # default as two teams, with 5 players
    # Game Rule (2,3,30) or (1,2,15)
    # Test
    vector = [2, 3, 5]
    print(utility.weighted_sections(vector))  # Output: [(0, 0.2), (0.2, 0.5), (0.5, 1.0)]