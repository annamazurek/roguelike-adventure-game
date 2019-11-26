def display_board(board, hero):
    '''
    Displays complete game board on the screen
    

    Returns:
    Nothing 
    '''

    for i in range(len(board)):
        if i in range(len(hero)):
            print(f"{hero[i].ljust(15) + ''.join(board[i])}")
        else:
            print(f"{15*' ' + ''.join(board[i])}")


def display_ascii(ascii_art):
    print(ascii_art)
    