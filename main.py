from helpers import *
import engine
import ui
import end_game
import hero_info

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

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
    return player


def change_position(movement, player, board):
    new_y = player['y'] + movement[0]
    new_x = player['x'] + movement[1]
    if board[new_y][new_x] == '#':
        pass
    else:
        player['y'] += movement[0]
        player['x'] += movement[1]
    return player


def main():

    clear_screen()
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.put_player_on_board(board, player)
    ui.display_board(board)


    is_running = True
    while is_running:
        key = key_pressed()
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        player["actual_stats"] = hero_info.actual_stats
        hero_statistics = player["actual_stats"]

        if key == 'q':
            is_running = False

        if key == 'z':
            clear_screen()
        else:           
            
            last_position = [player['y'], player['x']]
            if key in 'wsad':
                change_position(CONTROL_DICT[key], player, board)
            board = engine.put_player_on_board(board, player, last_position)
            clear_screen()

            hero = hero_info.list_hero_stats(hero_statistics)
            ui.display_board(board, hero)

    # end = 'win'  # the 'end' depends from the life of Necromancer-rat
    end_game.end_game(end)  # the parameters: 'win' or 'lose'



if __name__ == '__main__':
    main()