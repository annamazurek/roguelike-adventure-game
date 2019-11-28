from helpers import *
import engine
import ui
import end_game
import duel
# from start_menu import *

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
# PLAYER_NAME = input("What is your name?")  # to change
# PLAYER_RACE = "elf"  # to change - zamiast inputa wywołanie funkcji zwracającej rasę
# PLAYER_CLASS = "rouge"  # to change - zamiast inputa wywołanie funkcji zwracającej klasę
# PLAYER_CHARACTER = "Neutral"  # to change - zamiast inputa wywołanie funkcji zwracającej charakter


BOARD_WIDTH = 80
BOARD_HEIGHT = 30
map_elements = []

CONTROL_DICT = {
    'w':[-1,0],
    's':[1,0],
    'a':[0,-1],
    'd':[0,1]
}


def create_player(usr_name, race, hero_class):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    # player position and look
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["name"] = usr_name
    player["race"] = race
    player["class"] = hero_class
    player["max_HP"] = 10
    player["max_mana"] = 10
    player["stats"] = {
        'HP': 10,
        'Mana': 10,
        'Level': 1,
        'STR': 10,
        'DEX': 10,
        'CON': 10,
        'INT': 10,
        'WIS': 10,
        'CHA': 10,
    }
    player['Kills'] = 0
    player["items"] = hero_items(player)
    player['Map'] = 0
    return player


def list_stats(statistics, player):
    info = [player["name"], player["race"], player["class"]]
    info.append(f"HP: {statistics['HP']}/{player['max_HP']}")
    info.append(f"Mana: {statistics['Mana']}/{player['max_mana']}")
    for key, value in list(statistics.items())[2:]:
        info.append(f"{key}: {value}")
    info.append(f"Kills: {player['Kills']}")
    info.append(f"Map: {player['Map']}")
    return info

# TOTALLY NEW
def change_level(which_lvl):
    # NEW LEVEL SCREEN

    # we can add le LEVEL and stats here
    if which_lvl == 0:
        new_map = 'mapLVL2.txt'
    elif which_lvl == 1:
        new_map = 'mapLVL3.txt'
    else:
        new_map = 'map.txt'
    new_position = {'x': 4, 'y': 4}
    # clear whole screen
    which_lvl += 1
    clear_screen()

    # show some screen about changing level

    # board = load new map
    board = engine.read_map(new_map)
    # player stays the same

    # lvl up?
    # back to the main loop
    return [new_position, board, which_lvl]
# TOTALLY NEW

def hero_items(player):
    #added accesories
    items = {"Weapon": [], "Armour": [], "Potions": [], "Accesories": []}
    if player['class'] == "Wizzard":
        items["Weapon"] = ["Wand"]
        items["Armour"] = ["Leather helmet"]
        items["Potions"] = ['Health potion']
    elif player['class'] == "Knight":
        items["Weapon"] = ["Sword"]
        items["Armour"] = ["Helmet", "Shield", "Heavy armour"]
        items["Potions"] = ['Health potion']
    elif player['class'] == "Rouge":
        items["Weapon"] = ["Daggers"]
        items["Armour"] = ["Leather helmet", "Leather armour"]
        items["Potions"] = ['Health potion']
    return items

def add_hero_item(player_obj, type_of_item, item_name):
    player_obj['items'][type_of_item].append(item_name)
    return player_obj


def check_level(player_obj):
    kills = player_obj['Kills']
    player_stats = player_obj['stats']
    if kills == 1:
        player_stats = {
        'HP': 500,
        'Mana': 20,
        'Level': 2,
        'STR': 500,
        'DEX': 20,
        'CON': 15,
        'INT': 15,
        'WIS': 15,
        'CHA': 15,
    }
        #lvl up
        pass
    if kills == 5:
        player_stats = {
        'HP': 50,
        'Mana': 30,
        'Level': 3,
        'STR': 20,
        'DEX': 20,
        'CON': 20,
        'INT': 20,
        'WIS': 20,
        'CHA': 20,
    }     
        #lvl up
        pass
    if kills == 12:
        player_stats = {
        'HP': 75,
        'Mana': 50,
        'Level': 4,
        'STR': 25,
        'DEX': 25,
        'CON': 25,
        'INT': 25,
        'WIS': 25,
        'CHA': 25,
    }        
        #lvl up
        pass
    if kills == 20:
        player_stats = {
        'HP': 100,
        'Mana': 75,
        'Level': 5,
        'STR': 30,
        'DEX': 30,
        'CON': 30,
        'INT': 30,
        'WIS': 30,
        'CHA': 30,
    }
        #lvl up
        pass
    return player_stats


# def stats_to_list(player):
#     stats_list=[]
#     for key, value in player():
#         stats_list.append(f'{key}: {value}')
#     return stats_list

def change_position(movement, player, board):

    y_pos = 0
    x_pos = 1

    new_board = False
    new_item = False
    new_kill = False
    is_final_battle = False

    new_y = player['y'] + movement[y_pos]
    new_x = player['x'] + movement[x_pos]

    if board[new_y][new_x] == '█':
        map_ele = '.'
        pass
    #########################################33
    elif board[new_y][new_x] == '/':
        if 'Door key' not in player['items']['Accesories']:
            ui.display_dialog_window('You need to hold a door key to access this area!')
            key_pressed()
            map_ele = '.'
        else:
            player['y'] += movement[0]
            player['x'] += movement[1]
            player['items']['Accesories'].remove('Door key')
            map_ele = '_'
    #########################################
    else:
        map_ele = board[new_y][new_x]
        player['y'] += movement[0]
        player['x'] += movement[1]
    
    if board[new_y][new_x] in '*GSW': 
        enemy_kind = board[new_y][new_x]
        duel_return_obj = duel.duel_menu(player['stats'], enemy_kind)
        map_ele = 'x'
        is_not_dead = duel_return_obj[2]
        is_final_battle = duel_return_obj[1]
        if is_not_dead:
            new_kill = True
        # check if player is dead and move - alive->move dead->finish
    #################################################################
    if board[new_y][new_x] == '#':
        # change lvl #TOTALY NEW
        change_the_level = change_level(player['Map'])
        player = change_the_level[0]
        new_board = change_the_level[1]
        player['Map'] = change_the_level[2]
        map_ele = '.'
        pass
    #################################################################        
    if board[new_y][new_x] == '!':  #
        ui.display_dialog_window('hello')  #
        key = key_pressed().lower()  #
        while True:  #
            if key == "1":  #
                ui.display_dialog_window('hello1')
            elif key == "2":
                ui.display_dialog_window('hello2')
            elif key == "3":
                break
            key = key_pressed().lower()
            if key == "c":
                break  #
    if board[new_y][new_x] == '?':  #
        ui.display_dialog_window('hello')  #


    if board[new_y][new_x] == '$':
        player = add_hero_item(player, 'Accesories', 'Door key')
        new_item = True
        map_ele = '.'
    

    return [map_ele, new_board, player, new_item, new_kill, is_final_battle] 
    # TOTALY NEW

def play_game(player, board):
    ui.display_dialog_window(
        "You are a Hero. Leading a wasteful life, you are running out of money. Fortunately, you have\nheard that in the nearby village of Codecools Gate, residents will generously pay for getting\nrid of the rat plague, so you decided to quickly hit the road to anticipate the competitors.\n\nRiding the village on your musk deer, you hear the screams of a villager.\n\nPress 'C' to continue.")  #            
    while True:  #
        key = key_pressed().lower()  #
        if key == "c":  #
            clear_screen()  #
            hero = list_stats(player['stats'], player)  #
            ui.display_board(board, hero)  #
            ui.display_dialog_window("To interact with NPC('!', '?') and monsters ('*', 'G', 'N', 'S') just go to their place.\nMove your character with keys: 'W', 'A', 'S', 'D'.")  #

            while True:
                key = key_pressed().lower()
                # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
                last_position = [player['y'], player['x']]
                # hero_statistics = player["stats"]
                hero = list_stats(player['stats'], player)  # Create a list of hero stats
                items = player['items']
                if key == 'q':
                    break
                elif key == 'i':
                    clear_screen()
                    while True:
                        ui.display_items(items)
                        key = key_pressed().lower()
                        if key == 'q':
                            break
                elif key == 'z':
                    clear_screen()
                elif key in 'wsad':
                    # TOTALY NEW
                    changing_position = change_position(CONTROL_DICT[key], player, board)
                    player['Map'] = changing_position[2]['Map']
                    map_elements.insert(0, changing_position[0])
                    if changing_position[1] != False:
                        board = changing_position[1]
                        player['x'] = changing_position[2]['x']
                        player['y'] = changing_position[2]['y']
                        # player['stats'] = changing_position[2]['stats']
                    elif changing_position[3] != False:
                        player = changing_position[2]
                        ui.display_dialog_window('You gained new item!')
                        # print(player)
                        key_pressed()
                    elif changing_position[4] != False:
                        player["Kills"] += 1
                        player['stats'] = check_level(player)
                    board = engine.put_player_on_board(board, player, map_elements, last_position)
                    # TOTALY NEW
                clear_screen()    
                if player['stats']['HP'] <= 0:
                    end = end_game.end_game('die')  # the 'end' depends from the life of Necromancer-rat
                    # clear_screen()
                    break
                elif changing_position[5] != False:
                    end_game.end_game('win')
                    key_pressed()
                    break

                ui.display_board(board, hero)
            break


def main(name, race, hero_class):
    clear_screen()
    player = create_player(name, race, hero_class)
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.read_map('map.txt')
    board = engine.put_player_on_board(board, player, map_elements)
    hero = list_stats(player['stats'], player)
    ui.display_board(board, hero)
    
    play_game(player, board)
    #end_game.end_game(end = None)  #
    restart_game()

def restart_game():
    print('Press to continue')
    key = key_pressed()


if __name__ == '__main__':
    main()
end_game.end_game('win')