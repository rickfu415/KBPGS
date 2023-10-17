"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""

import random
import player
import utility


class Team():
    def __init__(self, Name, ID, rule):
        self.Name = Name
        self.ID = ID
        self.status = "None" # either in Offense or Defense
        self.current_score = 0
        self.player_list = []
        self.player_weights = [0.2, 0.2, 0.2, 0.2, 0.2] # needs to be based on capability
        self.offense_probability_range = None
        self.game_rule = {"Mid-range":rule[0], "Three-pointer":rule[1], "Layup":rule[0]}
        self.statistics = {}
    
    def assemble(self): # call after all players are added
        self.player_weights = [0.2, 0.2, 0.2, 0.2, 0.2] # needs to be based on capability
        self.offense_probability_range = utility.weighted_sections(self.player_weights)
        print("Team",self.Name,"has",len(self.player_list),"players")
        print("Team",self.Name,"offense_probability_range",self.offense_probability_range)



    def add_player(self, p):
        self.player_list.append(p)
        if len(self.player_list)>5:
            print("Team",self.Name,"has More than 5 player!")
    
    def offense(self):
        which_player_to_offense = utility.find_range(random.uniform(0, 1), self.offense_probability_range)
        result = self.player_list[which_player_to_offense].offense()
        if (result==-1):
            #print("Team",self.Name,"had a turnover")
            return
        if (result>0):
            self.current_score += result
            #print("Team",self.Name,"score now is",self.current_score)
        return
    
    def summary(self):
        print("-"*120)
        print("Team",self.Name,"total points:",self.current_score)
        for p in self.player_list:
            p.summary()
