from helpers import *
import random
import monster
import time
import end_game

HP = 'HP'
MANA = 'Mana'
STR = 'STR'
DEX = 'DEX'
CON ='CON'
INT ='INT'
WIS ='WIS'
CHA = 'CHA'



def player_profile():
    # return [playerATK, playerHP, and other stuff] 
    return [5, 50]


def monster_profile():
    # resturn [monsterATK, and stuff]
    return {
        'STR': 2,
        'HP': 16,
        'MANA': 0,
        'DEX': 5,
        'CON': 5,
        'INT': 5,
        'WIS': 5,
        'CHA': 5}


def update_health(amount, hit):
    hp = amount - hit
    return hp


def update_mana(amount, hit):
    pass

def print_player_stats(player_stats):
    for stat in player_stats:
        print(f"{stat} : {player_stats[stat]}")


def print_fight(player, monster):
    print('PLAYER')
    print_player_stats(player)
    print('PRESS c to attack')
    print_player_stats(monster)
    pass

def print_attack(amount):
    if amount == 0:
        print('you"ve MISSED')
    else:
        print(f"you've dealt {amount} dmg")

def print_monster_attack(amount):
    if amount == 0:
        print('Monster missed')
    else:
        print(f'Monster dealt {amount} damage to you')


def handle_fight(key, player):
    attack = 0
    if key == 'c':
        # weapon attack
        # calculate amount of dmg
        dodge = random.randint(1, 20)
        if player[DEX] >= dodge-10:
            attack_modifier = random.randint(-4,4)
            attack = player[STR] + attack_modifier
        else:
            attack = 0
    if key == 's':
        pass
        # spell attack
    return attack

def monster_attack(monster):

    choose_attack = random.randint(1,3)

    if choose_attack == 1:
        attack = monster[STR]
    if choose_attack == 2:
        attack = monster[INT]
    if choose_attack == 3:
        attack = monster[CHA]

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
    # start duel screen

    hp = 'hp'
    dmg = 'dmg'

    is_running = True
    player_not_dead = True
    while is_running and player_not_dead:


        # clear screen
        clear_screen()
        # display fight screen
        print_fight(player, monster)
        # input with player turn
        key = key_pressed()
        
        # check what kind of dmg and calculate it
        hit = handle_fight(key, player)
        
        # change hp of monster + print amount of dmg dealt and wait 0.5 s
        monster[HP] = update_health(monster[HP], hit)
        print_attack(hit)
        time.sleep(.8)
        
        # clear and show updated hp/mana
        clear_screen()
        print_fight(player, monster)

        #check if monster is not dead - if is is break the fight -- TO DO end fight screen + some items mb?
        is_running = check_if_dead(monster[HP])
        if is_running == False:
            pass
        else:
            # monster turn
            player[HP] = update_health(player[HP], monster_attack(monster))
            print_monster_attack(monster_attack(monster))
            time.sleep(.8)
            clear_screen()
            print_fight(player, monster)
            player_not_dead = check_if_dead(player[HP])

        # if player_not_dead == False:
        #     end_game.end_game('die')
        # else next turn


        # if one of them dead - Finish screen - Loot? NEEDS TO BE FIXED INTO ONE FUNCTION CHECKOUTPUT
        # back to the game

    return player
