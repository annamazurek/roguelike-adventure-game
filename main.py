from helpers import *
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30


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




def main():

    player = create_player()

    is_running = True
    
    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        if key == 'z':
            clear_screen()
        else:
            if key == 'w':
                engine.change_position(-1,0,player)
            if key == 's':
                engine.change_position(1,0,player)
            if key == 'a':
                engine.change_position(0,-1,player)
            if key == 'd':
                engine.change_position(0,1,player)
            print(key)
            clear_screen()
            board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
            board = engine.put_player_on_board(board, player)
            ui.display_board(board)


if __name__ == '__main__':
    main()