import helpers
import ui
import class_menu

choose_rase = """

                                             ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗    ██████╗  █████╗ ███████╗███████╗   
                                            ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╗
                                            ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██████╔╝███████║███████╗█████╗  ╚═╝
                                            ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██╔══██╗██╔══██║╚════██║██╔══╝  ██╗
                                            ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ██║  ██║██║  ██║███████║███████╗╚═╝
                                            ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝                                                       """

human = """

                                                                ██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
                                                                ██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║
                                                                ███████║██║   ██║██╔████╔██║███████║██╔██╗ ██║
                                                                ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
                                                                ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
                                                                ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                  """

halfling = """

                                                        ██╗  ██╗ █████╗ ██╗     ███████╗██╗     ██╗███╗   ██╗ ██████╗ 
                                                        ██║  ██║██╔══██╗██║     ██╔════╝██║     ██║████╗  ██║██╔════╝ 
                                                        ███████║███████║██║     █████╗  ██║     ██║██╔██╗ ██║██║  ███╗
                                                        ██╔══██║██╔══██║██║     ██╔══╝  ██║     ██║██║╚██╗██║██║   ██║
                                                        ██║  ██║██║  ██║███████╗██║     ███████╗██║██║ ╚████║╚██████╔╝
                                                        ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                                           """

dwarf = """

                                                                ██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
                                                                ██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝
                                                                ██║  ██║██║ █╗ ██║███████║██████╔╝█████╗  
                                                                ██║  ██║██║███╗██║██╔══██║██╔══██╗██╔══╝  
                                                                ██████╔╝╚███╔███╔╝██║  ██║██║  ██║██║     
                                                                ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝                                                                           """

elf = """

                                                                            ███████╗██╗     ███████╗
                                                                            ██╔════╝██║     ██╔════╝
                                                                            █████╗  ██║     █████╗  
                                                                            ██╔══╝  ██║     ██╔══╝  
                                                                            ███████╗███████╗██║     
                                                                            ╚══════╝╚══════╝╚═╝                                                                                 """


def start_menu_structure():
    menu = [human, halfling, dwarf, elf]
    instruction = "TO NAVIGATE USE 'A'- KEY TO MOVE LEFT OR 'D' KEY TO MOVE RIGHT"
    # 88
    title =  choose_rase

    return [title, menu, instruction]


# LATER TO UI
def print_menu(menu_structure, num_of_option):
    
    TITLE = 0
    MENU_COMPONENTS = 1
    INSTRUCTION = 2
    LENGHT_OF_LINE = len("                        ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╗")

    print('{:^0}'.format(menu_structure[TITLE]))
    print()
    print('{:^100}'.format(menu_structure[MENU_COMPONENTS][num_of_option]))
    print()
    print(f'{menu_structure[INSTRUCTION].center(LENGHT_OF_LINE)}')
    print('{:^106}'.format('Press "C" to confirm'))


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
        output = move_forward(option)
    return output, num_of_option


def handle_menu_option(number_to_check):
    MENU_OPTIONS = 1
    if number_to_check < 0:
        number_to_check = len(start_menu_structure()[MENU_OPTIONS])-1
    elif number_to_check == len(start_menu_structure()[MENU_OPTIONS]):
        number_to_check = 0
    return number_to_check


def move_forward(where):
    output = True
    if where == 0:
        helpers.clear_screen()
        print(human)
        input()
        
        
    elif where == 1:
        helpers.clear_screen()
        print(halfling)
        input()
        
        
    elif where == 2:
        helpers.clear_screen()
        print(dwarf)
        input()
        
        
    elif where == 3:
        helpers.clear_screen()
        print(elf)
        input()
        
        
    elif where == 9:
        # go to LEAVE
        output = False
        
    class_menu.start_menu()
    return output


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