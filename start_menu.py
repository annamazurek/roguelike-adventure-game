import helpers
import ui
import race_menu
import load_highscore


def start_menu_structure():
    start = """
                                                                       ███████╗████████╗ █████╗ ██████╗ ████████╗
                                                                       ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
                                                                       ███████╗   ██║   ███████║██████╔╝   ██║   
                                                                       ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   
                                                                       ███████║   ██║   ██║  ██║██║  ██║   ██║   
                                                                       ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝ """
    high_score = """ 
                                                        ██╗  ██╗██╗ ██████╗ ██╗  ██╗    ███████╗ ██████╗ ██████╗ ██████╗ ███████╗   
                                                        ██║  ██║██║██╔════╝ ██║  ██║    ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
                                                        ███████║██║██║  ███╗███████║    ███████╗██║     ██║   ██║██████╔╝█████╗ 
                                                        ██╔══██║██║██║   ██║██╔══██║    ╚════██║██║     ██║   ██║██╔══██╗██╔══╝  
                                                        ██║  ██║██║╚██████╔╝██║  ██║    ███████║╚██████╗╚██████╔╝██║  ██║███████╗
                                                        ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ """
    exit_game = """
                                                                            ███████╗██╗  ██╗██╗████████╗
                                                                            ██╔════╝╚██╗██╔╝██║╚══██╔══╝
                                                                            █████╗   ╚███╔╝ ██║   ██║   
                                                                            ██╔══╝   ██╔██╗ ██║   ██║   
                                                                            ███████╗██╔╝ ██╗██║   ██║   
                                                                            ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ """

    menu = [start, high_score,exit_game]
    # 88
    instruction = "TO NAVIGATE USE 'A'- KEY TO MOVE LEFT OR 'D' KEY TO MOVE RIGHT"
    title = """

                                ██████╗  █████╗ ███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗███████╗       ██╗       ██████╗  █████╗ ████████╗███████╗
                                ██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██╔════╝       ██║       ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                                ██████╔╝███████║███████╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ███████╗    ████████╗    ██████╔╝███████║   ██║   ███████╗
                                ██╔══██╗██╔══██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ╚════██║    ██╔═██╔═╝    ██╔══██╗██╔══██║   ██║   ╚════██║
                                ██████╔╝██║  ██║███████║███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ███████║    ██████║      ██║  ██║██║  ██║   ██║   ███████║
                                ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝    ╚═════╝      ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                                                                     

                                                                                                     ____-----__
                                                                                                 .--'           `\ 
                                                                                               .'                 `.
                                                                                             .'                     \ 
                                                                               _______     .'                        `.
                                                                      ____,---'   ~~~<.---'                            \ 
                                                                    _C~           `--'                                  \ 
                                                           __--x_x-'  .~      `---'                                      `
                                                          | /         \'                                                  |
                                                           \|                                                             |
                                                            \   \  ,                                             __       `,
                                                             `~~ ~~ --__                                       .'  \       |
                                                              `` \_                                          '     |      |
                                                                   `-._                                     /       `    /
                                                                       `-.___/--.              /           /         |  /
                                                                                 `~~--__       \          /          | <
                                                                                __>     `,     >         |          /   \ 
                                                                            .--'         /   ,'`---.___ .'           /   `.
                                                                          .'    ___.---'/   /           |           /      `.___
                                                                        .'   .~~    .--'   /         ____\_      __/ \          `.
                                                                        |'/\|      /,   __,'        ////   `----'     `.__        `,
                                                                        \'         `/._/                                 `---.."   |
                                                                                    `'                                 __..--'    .'
                                                                                                                    .'         .'
                                                                                                                 .'   .------'
                                                                                                                 |  .'
                                                                                                         ______.'   |
                                                                                                        .'         .'
                                                                                         __====_`-----'  .-------'
                                                                                                `-------'
                                                                                                                                                                                   """
    return [title, menu, instruction]


# LATER TO UI
def print_menu(menu_structure, num_of_option):
    
    TITLE = 0
    MENU_COMPONENTS = 1
    INSTRUCTION = 2
    LENGHT_OF_LINE = 200

    print('{:^0}'.format(menu_structure[TITLE]))
    print()
    print('{0:<0}{2:^200}{1:>0}'.format('','',menu_structure[MENU_COMPONENTS][num_of_option]))
    print()
    print(f'{menu_structure[INSTRUCTION].center(LENGHT_OF_LINE)}')
    print('{:^200}'.format('Press "C" to confirm'))
    print(num_of_option)


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
        race_menu.race_start_menu()
        pass
    elif where == 1:
        helpers.clear_screen()
        load_highscore.print_highscore(load_highscore.sort_score(load_highscore.read_file('highscore.txt')))
        input()
        pass
    elif where == 2:
        # go to LEAVE
        output = False
    return output


def begin_start_menu():
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
        

begin_start_menu()