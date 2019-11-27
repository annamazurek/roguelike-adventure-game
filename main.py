from helpers import *
import engine
import ui
import end_game
import duel

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30
map_elements = []

CONTROL_DICT = {
    'w':[-1,0],
    's':[1,0],
    'a':[0,-1],
    'd':[0,1]
}


def create_player(name, race, hero_class):
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
    player["name"] = name
    player["race"] = race
    player["class"] = hero_class
    player["max_HP"] = 10
    player["max_mana"] = 10
    player["stats"] = {
        'HP': 10,
        'Mana': 10,
        'STR': 10,
        'DEX': 10,
        'CON': 10,
        'INT': 10,
        'WIS': 10,
        'CHA': 10
    }
    player["items"] = hero_items(player)
    global HERO_STATS
    HERO_STATS = player["stats"]
    return player


def list_stats(statistics, player):
    info = [player["name"], player["race"], player["class"]]
    info.append(f"HP: {statistics['HP']}/{player['max_HP']}")
    info.append(f"Mana: {statistics['Mana']}/{player['max_mana']}")
    for key, value in list(statistics.items())[2:]:
        info.append(f"{key}: {value}")
    return info


def hero_items(player):
    items = {"Weapon": [], "Armour": [], "Potions": []}
    if player["class"] == "wizzard":
        items["Weapon"] = ["Wand"]
        items["Armour"] = ["Leather helmet"]
    elif player["class"] == "knight":
        items["Weapon"] = ["Sword"]
        items["Armour"] = ["Helmet", "Shield", "Heavy armour"]
    elif player["class"] == "rouge":
        items["Weapon"] = ["Daggers"]
        items["Armour"] = ["Leather helmet", "Leather armour"]
    return items

# def stats_to_list(player):
#     stats_list=[]
#     for key, value in player():
#         stats_list.append(f'{key}: {value}')
#     return stats_list

def change_position(movement, player, board):

    y_pos = 0
    x_pos = 1

    new_y = player['y'] + movement[y_pos]
    new_x = player['x'] + movement[x_pos]

    if board[new_y][new_x] == '█':
        map_ele = '.'
        pass
    else:
        map_ele = board[new_y][new_x]
        player['y'] += movement[0]
        player['x'] += movement[1]
    
    if board[new_y][new_x] == '*': 
        duel.duel_menu(player['stats'])
        map_ele = 'x'
        # check if player is dead and move - alive->move dead->finish
    if board[new_y][new_x] in '?!':
        ui.display_dialog_window('hello')
        key_pressed()

    return map_ele


def play_game(player, board):
    while True:
        key = key_pressed().lower()
        # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        last_position = [player['y'], player['x']]
        # hero_statistics = player["stats"]
        hero = list_stats(player['stats'], player)  # Create a list of hero stats
        items = hero_items(player)
        if key == 'q':
            break
        elif key == 'i':
            clear_screen()
            while True:
                ui.display_items(items)
                key = key_pressed().lower()
                if key == 'q':
                    print('q')
                    break
                else:
                    clear_screen()
        elif key == 'z':
            clear_screen()
        elif key in 'wsad':
            map_elements.insert(0, change_position(CONTROL_DICT[key], player, board))
            board = engine.put_player_on_board(board, player, map_elements, last_position)
        clear_screen()
        if player['stats']['HP'] <= 0:
            break
        
        ui.display_board(board, hero)


def main():
    clear_screen()
    player = create_player("Janusz", "Elf", "rouge")
    board = engine.read_map('map.txt')
    board = engine.put_player_on_board(board, player, map_elements)
    hero = list_stats(player['stats'], player)
    ui.display_board(board, hero)
    ui.display_dialog_window("Hello Adventurer!")

    play_game(player, board)


    if player['stats']['HP'] <= 0:
        end = 'die'
    else:
        end = 'win'  # the 'end' depends from the life of Necromancer-rat

    clear_screen()
    # end = 'win'  # the 'end' depends from the life of Necromancer-rat

    end_game.end_game(end)  # the parameters: 'win' or 'lose'
    restart_game()

def restart_game():
    print('restart y/n?')
    key = key_pressed()
    if key == 'y':
        main()
    else:
        print('bb')



if __name__ == '__main__':
    main()
