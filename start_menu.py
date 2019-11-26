import helpers
import ui

def menu_structure():
    menu = ['START GAME', 'HIGHSCORE']
    title = ''
    exit_ = ''

    return [title, menu, exit_]


def menu_handler(key):
    
    # ask user for input
    print(key)
    output = True
    if key == '0':
        output = False
    return output


def menu():
    is_running = True
    while is_running:
        # clear screen //helpers.clear_screen?
        # print menu structure //ui.print_menu?
        # wait for user input 
        key = helpers.key_pressed()
        # call menu handler with user input 
        is_running = menu_handler(key)
        


menu()