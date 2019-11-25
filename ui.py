def display_board(board):
    '''
    Displays complete game board on the screen
    

    Returns:
    Nothing 
    '''
    for row in board:
        for col in row:
            print(col, end = '')
        print('', end = '\n')