from helpers import *


def player_profile():
    # return [playerATK, playerHP, and other stuff] 
    return [5, 50]


def monster_profile():
    # resturn [monsterATK, and stuff]
    return {'dmg': 2,
    'hp': 16}


def update_health(amount, hit):
    hp = amount - hit
    return hp


def update_mana(amount, hit):
    pass


def print_fight(player, monster):
    atk = 'dmg'
    hp = 'hp'
    print('PLAYER')
    print(f"atk: {player[atk]}")
    print(f"hp: {player[hp]}")
    print('PRESS c to attack')
    print('MONSTER')
    print(f"atck: {monster[atk]}")
    print(f"hp: {monster[hp]}")
    pass


def handle_fight(key, player):
    dmg = 'dmg'
    attack = 0
    if key == 'c':
        # calculate amount of dmg
        attack = player[dmg]
    return attack


def check_if_dead(hp):
    output = True
    if hp <= 0:
        output = False
    return output


def duel_menu(player_stats):

    # inicialize fight/////create object of monster/player?
    player = player_stats
    monster = monster_profile()
    

    hp = 'hp'
    dmg = 'dmg'

    is_running = True
    while is_running:


        # clear screen
        clear_screen()
        # display fight screen
        print_fight(player,monster)
        # input with player turn
        key = key_pressed()
        hit = handle_fight(key, player)
        monster[hp] = update_health(monster[hp], hit)
        # monster turn
        player[hp] = update_health(player[hp], monster[dmg])

        # if one of them dead - Finish screen - Loot? NEEDS TO BE FIXED INTO ONE FUNCTION CHECKOUTPUT
        is_running = check_if_dead(player[hp])
        is_running = check_if_dead(monster[hp])
        # back to the game

    return player
