"""
Kentucky Basketball Pickup Game Simulator

Author: Rui(Rick) Fu
Date: 09-22-2023
"""


import random
import player
import game
import team


def single_game_run():
    number_of_players = 5
    HomeTeam = team.Team("Home", 1)
    for i in range(1, number_of_players+1):
        name = "Home_player_" + str(i)
        ID = i
        _player = player.Player(name, ID)
        _player.mid_range_shoot += random.uniform(-0.1, 0.1)
        _player.layup += random.uniform(-0.1, 0.1)
        _player.three_pointer += random.uniform(-0.1, 0.1)
        _player.initialize()
        _player.show()
        HomeTeam.player_list.append(_player)
    HomeTeam.assemble()

    GuestTeam = team.Team("Guest", 2)
    for i in range(1, number_of_players+1):
        name = "Guest_player_" + str(i)
        ID = i
        _player = player.Player(name, ID)
        _player.mid_range_shoot += random.uniform(-0.1, 0.1)
        _player.layup += random.uniform(-0.1, 0.1)
        _player.three_pointer += random.uniform(-0.1, 0.1)
        _player.initialize()
        _player.show()
        GuestTeam.player_list.append(_player)
    GuestTeam.assemble()

    rule = (2, 3, 30)
    ID = 1
    singleGame = game.Game(rule, ID)
    singleGame.homeTeam = HomeTeam
    singleGame.guestTeam = GuestTeam

    print("Game:",ID)
    for round in range(1, int(1E2)):
        result = HomeTeam.offense()
        result = GuestTeam.offense()
        print("Round:(",round,")",
              HomeTeam.Name,"[",HomeTeam.current_score,
              ":",GuestTeam.current_score,"]",GuestTeam.Name,
              )
        if (HomeTeam.current_score>19):
            print("Team",HomeTeam.Name,"has WON!")
            break
        if (GuestTeam.current_score>19):
            print("Team",GuestTeam.Name,"has WON!")
            break
        
        #Update the records
        # singleGame.update()


    return


if __name__ == "__main__":
    # default as two teams, with 5 players
    # Game Rule (2,3,30) or (1,2,15)
    single_game_run()
