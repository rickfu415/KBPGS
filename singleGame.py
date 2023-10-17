"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""


import random
import player
import game
import team


def single_game_run(number_of_players, rule):
    
    HomeTeam = team.Team("Home", 1, rule)
    for i in range(1, number_of_players+1):
        name = "Home_player_" + str(i)
        ID = i
        _player = player.Player(name, ID, rule)
        _player.mid_range_shoot += random.uniform(-0.1, 0.1)    #adding some uncertainty 
        _player.layup += random.uniform(-0.1, 0.1)              #adding some uncertainty 
        _player.three_pointer += random.uniform(-0.1, 0.1)      #adding some uncertainty 
        _player.initialize()
        _player.show()
        HomeTeam.player_list.append(_player)
    HomeTeam.assemble()

    GuestTeam = team.Team("Guest", 2, rule)
    for i in range(1, number_of_players+1):
        name = "Guest_player_" + str(i)
        ID = i
        _player = player.Player(name, ID, rule)
        _player.mid_range_shoot += random.uniform(-0.1, 0.1)    #adding some uncertainty 
        _player.layup += random.uniform(-0.1, 0.1)              #adding some uncertainty 
        _player.three_pointer += random.uniform(-0.1, 0.1)      #adding some uncertainty 
        _player.initialize()
        _player.show()
        GuestTeam.player_list.append(_player)
    GuestTeam.assemble()

    
    ID = 1
    singleGame = game.Game(rule, ID)
    singleGame.homeTeam = HomeTeam
    singleGame.guestTeam = GuestTeam

    print("Game:",ID)
    end = False
    for round in range(1, int(1E4)):
        result = HomeTeam.offense()
        if (HomeTeam.current_score>=rule[2]):
            print("Team",HomeTeam.Name,"has WON!")
            end = True
        else:
            result = GuestTeam.offense()
        if (GuestTeam.current_score>=rule[2]):
            print("Team",GuestTeam.Name,"has WON!")
            end = True

        print("Round:(",round,")",
              HomeTeam.Name,"[",HomeTeam.current_score,
              ":",GuestTeam.current_score,"]",GuestTeam.Name,
              )
        if (end): break

    HomeTeam.summary()
    GuestTeam.summary()
    return


if __name__ == "__main__":
    # default as two teams, with 5 players
    # Game Rule (2,3,30) or (1,2,15)
    rule = (2, 3, 30)
    rule = (1, 2, 15)
    number_of_players = 5
    single_game_run(number_of_players, rule)
