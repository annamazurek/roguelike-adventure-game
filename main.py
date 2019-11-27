from helpers import *
import engine
import ui
import end_game
# import hero_info

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
PLAYER_NAME = input("What is your name?")  # to change
PLAYER_RACE = "elf"  # to change - zamiast inputa wywołanie funkcji zwracającej rasę
PLAYER_CLASS = "rouge"  # to change - zamiast inputa wywołanie funkcji zwracającej klasę
PLAYER_CHARACTER = "Neutral"  # to change - zamiast inputa wywołanie funkcji zwracającej charakter


BOARD_WIDTH = 80
BOARD_HEIGHT = 30

CONTROL_DICT = {
    'w':[-1,0],
    's':[1,0],
    'a':[0,-1],
    'd':[0,1]
}


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["name"] = PLAYER_NAME
    player["race"] = PLAYER_RACE
    player["class"] = PLAYER_CLASS
    player["char"] = PLAYER_CHARACTER
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


    return player

HERO_STATS = create_player()["stats"]  # hero actual stats


def list_stats(statistics, player):
    info = [player["name"], player["race"], player["class"], player["char"]]
    # for key in statistics[2:]:
    #     info.append(f"{player["stats"][key]}")
    info.append(f"HP: {statistics['HP']}/{player['max_HP']}")
    info.append(f"Mana: {statistics['Mana']}/{player['max_mana']}")
    for key, value in list(statistics.items())[2:]:
        info.append(f"{key}: {value}")
    return info


def hero_items():
    items = {"Weapon": [], "Armour": [], "Potions": []}
    if PLAYER_CLASS == "wizzard":
        items["Weapon"] = ["Wand"]
        items["Armour"] = ["Leather helmet"]
    elif PLAYER_CLASS == "knight":
        items["Weapon"] = ["Sword"]
        items["Armour"] = ["Helmet", "Shield", "Heavy armour"]
    elif PLAYER_CLASS == "rouge":
        items["Weapon"] = ["Daggers"]
        items["Armour"] = ["Leather helmet", "Leather armour"]
    return items


def change_position(movement, player, board):  # maybe plop it to the engine module?
    new_y = player['y'] + movement[0]
    new_x = player['x'] + movement[1]
    if board[new_y][new_x] == '#':
        pass
    else:
        player['y'] += movement[0]
        player['x'] += movement[1]
    return player


def play_game(player, board):
    while True:
        key = key_pressed().lower()
        # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        last_position = [player['y'], player['x']]
        # hero_statistics = player["stats"]
        hero = list_stats(HERO_STATS, player)  # Create a list of hero stats
        items = hero_items()
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
            change_position(CONTROL_DICT[key], player, board)
            board = engine.put_player_on_board(board, player, last_position)
        clear_screen()
        ui.display_board(board, hero)
        HERO_STATS['HP'] += 1
        HERO_STATS["Mana"] += 1


def main():
    clear_screen()
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.put_player_on_board(board, player)
    # when you want to change some statistic, type in your code i.e.:    player["stats"]["HP"] = 11  or  player["stats"]["STR"] += 1
    hero = list_stats(HERO_STATS, player)
    ui.display_board(board, hero)
    ui.display_dialog_window("Hello Adventurer!")

    play_game(player, board)
    clear_screen()
    # end = 'win'  # the 'end' depends from the life of Necromancer-rat
    end_game.end_game(end)  # the parameters: 'win' or 'lose'



if __name__ == '__main__':
    main()