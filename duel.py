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


def duel_stracture():
    duel = """

                                                                    ██████╗ ██╗   ██╗███████╗██╗        
                                                                    ██╔══██╗██║   ██║██╔════╝██║     ██╗
                                                                    ██║  ██║██║   ██║█████╗  ██║     ╚═╝
                                                                    ██║  ██║██║   ██║██╔══╝  ██║     ██╗
                                                                    ██████╔╝╚██████╔╝███████╗███████╗╚═╝
                                                                    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                       """
    
    rat_warrior = """
                                                                      ,     .         You will newer pass us,
                                                                      (\,;,/)           We will eat you to
                                                                       (o o)\//,              Death !
                                                                        \ /     \,
                                                                        `+'(  (   \    )
                                                                         //  //  \ |_./
                                                                        '~' '~----'       """
    skeleton = """

                                                                                  _.--""-._
                                                      .                         ."         ".
                                                     / \    ,^.         /(     Y             |       )\ 
                                                    /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
                                                    |        :|    `>   '.     l_..-------.._l      .'
                                                    |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
                                                    \  .-' | |  `              l._       _.'
                                                     \/    | |                   l`^^'^^'j
                                                           | |                _   \_____/     _
                                                           j |               l `--__)-'(__.--' |
                                                           | |               | /`---``-----'"1 |  ,-----.
                                                           | |               )/  `--' '---'   \|-'  ___  `-. 
                                                           | |              //  `-'  '`----'  /  ,-'   I`.  \ 
                                                         _ L |_            //  `-.-.'`-----' /  /  |   |  `. \ 
                                                        '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
                                                        `._;/7(-.......'  /        ) (     |  |            | | |
                                                         `._;l _'--------_/        )-'/     :  |___.    _._./ ;
                                                           | |                 .__ )-'\  __  \  \  I   1   / /
                                                           `-'                /   `-\-(-'   \ \  `.|   | ,' /
                                                                              \__  `-'    __/  `-. `---'',-'
                                                                                   )-._.-- (      `-----'
                                                                                )(  l\ o ('..
                                                                          _..--' _'-' '--'.-. |
                                                                    __,,-'' _,,-''            \ \ 
                                                                   f'. _,,-'                   \ \ 
                                                                  ()--  |                       \ \ 
                                                                    \.  |                       /  \ 
                                                                      \ \                      |._  |
                                                                       \ \                     |  ()|
                                                                        \ \                     \  /
                                                                        ) `-.                   | |
                                                                      // .__)                  | |
                                                                   _.//7'                      | |
                                                                '---'                         j_|
                                                                                            (| |
                                                                                             |  \ 
                                                                                             |lllj
                                                                                              |||||                                                                        
                """

    rat_boss = """
                                                                           ____
                                                               ________   |    |
                                                               \      /   |____|
                                                                \    /   _|____|_   
                                                                 \||/     /  oo`\    
                                                                  ||    .<     ___\*   
                                                                  ||\   /\ \.-.' \    
                                                                  || \ J  `.|`.\/ \  
                                                                  || | | _.|  | | |
                                                                  || /\/\  .'`.|-' /
                                                                  ||/   L   /|o`--'\ 
                                                                  ||    |  /\/\/\   \           
                                                                  ||    J /      `.__\ 
                                                                  ||    |/         /  \     
                                                                  ||     \\      .'`.  `..                                           .'
                                                                  ||    ___)_/\_(____`.  `-._______________________________________.'/
                                                                  ||   (___._/  \_.___) `-.________________________________________.-'
                """
    rat_1 = """

                                                                       __             _,-"~^"-.
                                                                     _// )      _,-"~`         `.
                                                                   ." ( /`"-,-"`                 ;
                                                                  / 6                             ;
                                                                 /           ,             ,-"     ;
                                                                (,__.--.      \           /        ;
                                                                //'   /`-.\   |          |        `._________
                                                                  _.-'_/`  )  )--...,,,___\     \-----------,)
                                                                 ((("~` _.-'.-'           __`-.   )         //
                                                                       ((("`             (((---~"`         //
                                                                                                           ((________________
                                                                                                            `----""""~~~~^^^```"""
    return [duel,[rat_warrior, skeleton, rat_boss, rat_1]]


def print_menu(duel_stracture_items, num_of_option = 1):   
    TITLE = 0
    MONSTERS = 1
    EXIT = 2

    print(f'{duel_stracture_items[TITLE]}')#
    
    print(f'{duel_stracture_items[MONSTERS][num_of_option]}')

    print('press any key to start a fight'.center(200,' '))


def player_profile():
    # return [playerATK, playerHP, and other stuff] 
    return [5, 50]


def monster_profile(which):
    # resturn [monsterATK, and stuff]
    if which == '*':
        enemy_stats = {
        'STR': 2,
        'HP': 16,
        'MANA': 0,
        'DEX': 5,
        'CON': 5,
        'INT': 5,
        'WIS': 5,
        'CHA': 5}
        pass
    elif which == "G":
        enemy_stats = {
        'STR': 10,
        'HP': 30,
        'MANA': 0,
        'DEX': 6,
        'CON': 5,
        'INT': 10,
        'WIS': 5,
        'CHA': 5}
        pass
    elif which == 'S':
        enemy_stats = {
        'STR': 20,
        'HP': 50,
        'MANA': 0,
        'DEX': 7,
        'INT': 15,
        'WIS': 5,
        'CHA': 5}
        pass
    else:
        enemy_stats = {
        'STR': 50,
        'HP': 100,
        'MANA': 50,
        'DEX': 10,
        'INT': 15,
        'WIS': 20,
        'CHA': 5}
    return enemy_stats


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


def duel_menu(player_stats, enemy_kind):


    # start duel screen
    is_final_battle = False
    hp = 'hp'
    dmg = 'dmg'
    # DUEL SCREEN
    enemy_draw = 0
    if enemy_kind == '*':
        enemy_draw = 0
    elif enemy_kind == 'G':
        enemy_draw = 3
    elif enemy_kind == 'S':
        enemy_draw = 1
    else:
        is_final_battle = True
        enemy_draw = 2
    clear_screen()
    print_menu(duel_stracture(),enemy_draw)
    key_pressed()


    # inicialize fight/////create object of monster/player?
    player = player_stats
    monster = monster_profile(enemy_kind)

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
        time.sleep(1)
        
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
            time.sleep(1)
            clear_screen()
            print_fight(player, monster)
            player_not_dead = check_if_dead(player[HP])

        # if player_not_dead == False:
        #     end_game.end_game('die')
        # else next turn


        # if one of them dead - Finish screen - Loot? NEEDS TO BE FIXED INTO ONE FUNCTION CHECKOUTPUT
        # back to the game

    return [player, is_final_battle, player_not_dead]