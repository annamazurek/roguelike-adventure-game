import helpers
import ui


def start_menu_structure():
    menu = ['START GAME', 'HIGHSCORE','EXIT']
    # 88
    title = '''
                     __      __  ___     ___   _____             __     __    _____  
                    |__) /\ /__`|__ |\/||__ |\ ||/__`    /\ |\ ||  \   |__) /\ |/__` 
                    |__)/~~\.__/|___|  ||___| \||.__/   /~~\| \||__/   |  \/~~\|.__/ 
'''

    return [title, menu]


# LATER TO UI
def print_menu(menu_structure, num_of_option):
    
    TITLE = 0
    MENU_COMPONENTS = 1
    EXIT = 2

    print('{:^0}'.format(menu_structure[TITLE]))
    print()
    print('{0:<0}{2:^100}{1:>0}'.format('<-a','d->',menu_structure[MENU_COMPONENTS][num_of_option]))
    print()
    print('{:^106}'.format('press c to confirm'))


def start_menu_handler(key, option):
    # ask user for input
    print(key)
    output = True
    if key == 'a':
        option -= 1
    if key == 'd':
        option += 1
    if key == '0':
        output = False
    num_of_option = handle_menu_option(option)

    if key == 'c':
        pass
    return output, num_of_option


def handle_menu_option(number_to_check):
    MENU_OPTIONS = 1
    if number_to_check < 0:
        number_to_check = len(start_menu_structure()[MENU_OPTIONS])-1
    elif number_to_check == len(start_menu_structure()[MENU_OPTIONS]):
        number_to_check = 0
    return number_to_check




def start_menu():
    is_running = True

    FIRST_ELEMENT = 0
    SECOND_ELEMENT = 1
    num_of_option = 0

    while is_running:
        helpers.clear_screen()
        # print menu structure //ui.print_menu?
        # wait for user input
        print_menu(start_menu_structure(), num_of_option)
        key = helpers.key_pressed()
        # call menu handler with user input
        menu_handler_options = start_menu_handler(key, num_of_option)
        is_running = menu_handler_options[FIRST_ELEMENT]
        num_of_option = menu_handler_options[SECOND_ELEMENT]
        

start_menu()