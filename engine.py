def create_board(width, height):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board 
    '''

    board = []
    upper = ['#']*width

    for row in range(height):
        line = []
        if row == 0 or row == height-1:
            board.append(upper)
        else:
            for col in range(width):
                if col == 0 or col == width-1:
                    line.append('#')
                else:
                    if col == 5:
                        line.append('#')
                    else:    
                        line.append('.')
            board.append(line)

    return board



    
def put_player_on_board(board, player, last_position=[1,1]):
    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
    POS_Y = 0
    POS_X = 1
    board[last_position[POS_Y]][last_position[POS_X]] = '.'
    board[player['y']][player['x']] = player['icon']

    return board
