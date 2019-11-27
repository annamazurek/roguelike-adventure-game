import helpers
import ui

choose_character =  """ 

                         ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗     ██████╗██╗  ██╗ █████╗ ██████╗  █████╗  ██████╗████████╗███████╗██████╗    
                        ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╗
                        ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██║     ███████║███████║██████╔╝███████║██║        ██║   █████╗  ██████╔╝╚═╝
                        ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██║     ██╔══██║██╔══██║██╔══██╗██╔══██║██║        ██║   ██╔══╝  ██╔══██╗██╗
                        ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║╚██████╗   ██║   ███████╗██║  ██║╚═╝
                        ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                                     
                """


wizzard = """  

                                                        ██╗    ██╗██╗███████╗███████╗ █████╗ ██████╗ ██████╗ 
                                                        ██║    ██║██║╚══███╔╝╚══███╔╝██╔══██╗██╔══██╗██╔══██╗
                                                        ██║ █╗ ██║██║  ███╔╝   ███╔╝ ███████║██████╔╝██║  ██║
                                                        ██║███╗██║██║ ███╔╝   ███╔╝  ██╔══██║██╔══██╗██║  ██║
                                                        ╚███╔███╔╝██║███████╗███████╗██║  ██║██║  ██║██████╔╝
                                                        ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 



                                                                                  ____ 
                                                                                .'* *.'
                                                                            __/_*_*(_
                                                                    ||    / _______ \ 
                                                                   |  |  /\_)/___\(_/\ 
                                                                  |  * |/ _((\- -/))_ \ 
                                                                 | * * *| \())(-)(()/ /
                                                                  \* #*/ ' \(((()))/ '
                                                                   \  /  /' \)).))/ ' \ 
                                                                    ||  /  # / _ \ - | \ 
                                                                   {||\/  ( .;''';. .'  )
                                                                    ||\__/    )\ __  /_/
                                                                    ||  \/  \   ' /  \/
                                                                    ||  (.'  '...' ' )
                                                                    ||    / /  |  \ \ 
                                                                    ||   / .   .   . \ 
                                                                    ||  /   .     .   \ 
                                                                    || /   /   |   \   \ 
                                                                    ||'   /    b    '.  '.
                                                                   .||    /     Bb     '-. '-._ 
                                                               .--''       /      BBb       '-.  '-.
                                                              (_____________\____.dBBBb.________)____)

                                                                    
                                            
                                            
                """
knight = """

                                                        ██╗  ██╗███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
                                                        ██║ ██╔╝████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
                                                        █████╔╝ ██╔██╗ ██║██║██║  ███╗███████║   ██║   
                                                        ██╔═██╗ ██║╚██╗██║██║██║   ██║██╔══██║   ██║   
                                                        ██║  ██╗██║ ╚████║██║╚██████╔╝██║  ██║   ██║   
                                                        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                               



                                                                              {} 
                                                                             .--.
                                                                            /.--.\ 
                                                                            |====|
                                                                            |`::`|
                                                                        .-;`\..../`;_.-^-._
                                                                /\    /  |...::..|`   :   `|
                                                                |:'\ |   /'''::''|   .:.   |
                                                               @|\ /\;-,/\   ::  |..:::::..|
                                                               `||\ <` >  >._::_.| ':::::' |
                                                                || `""`  /   ^^  |   ':'   |
                                                                ||       |       \    :    /
                                                                ||       |        \   :   /
                                                                ||       |___/\___|`-.:.-`
                                                                ||        \_ || _/    `
                                                                ||        <_ >< _>
                                                                ||        |  ||  |
                                                                ||        |  ||  |
                                                                ||        |  ||  |
                                                                ||        |  ||  |
                                                                ||       _\.:||:./_
                                                                \/      /____/\____\        


                                
                """
rouge = """

                                                        ██████╗  ██████╗ ██╗   ██╗ ██████╗ ███████╗
                                                        ██╔══██╗██╔═══██╗██║   ██║██╔════╝ ██╔════╝
                                                        ██████╔╝██║   ██║██║   ██║██║  ███╗█████╗  
                                                        ██╔══██╗██║   ██║██║   ██║██║   ██║██╔══╝  
                                                        ██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗
                                                        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝
                                          


                                                                              _A_
                                                                             / | \ 
                                                                            |.-=-.|
                                                                           )| * * |(
                                                                        .=='\ -  /`==.
                                                                      .'\   (`:')   /`.\ 
                                                            |\      /_ |_.-' : `-._|__ \ 
                                                            \ \     [__]'\    :   / `[__]
                                                             \ \   /  /   >=======<  /  /
                                                              \ \_/ .'   /  ,-:-.  \/=,'
                                                               \ \/ _/  |__/v^v^v\__) 
                                                                (\)    \ V^V^V^V^V|\_/
                                                                 \ \     \`---|---'/
                                                                          \-._|_,-/
                                                                           |__|__|
                                                                          <___X___>
                                                                           \..|../
                                                                            \ | /
                                                                            \ | /
                                                                            \ | /
                                                                            /V|V\ 
                                                                           /  |  \ 
                                                                          '--' `--` 
                                            


                """

dwarf = """

                                                        ██████╗ ██╗    ██╗ █████╗ ██████╗ ███████╗
                                                        ██╔══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝
                                                        ██║  ██║██║ █╗ ██║███████║██████╔╝█████╗  
                                                        ██║  ██║██║███╗██║██╔══██║██╔══██╗██╔══╝  
                                                        ██████╔╝╚███╔███╔╝██║  ██║██║  ██║██║     
                                                        ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     
                                                                                                
                                                                         _.-;-._
                                                                        ;_.JL___; 
                                                                        F"-/\_-7L
                                                                        | a/ e | \ 
                                                                       ,L,c;,.='/;,
                                                                    _,-;;S:;:S;;:' '--._
                                                                  ;. \;;s:::s;;: .'   /\ 
                                                                 /  \  ;::::;;  /    /  \ 
                                                                / ,  k ;S';;'S.'    j __,l
                                                            ,---/| /  /S   /S '.   |'   ;
                                                            ,Ljjj |/|.' s .' s   \  L    |
                                                            LL,_ ]( \    /    '.  '.||   ;
                                                         ||\ > /  ;-.'_.-.___\.-'(|=="(
                                                          JJ," /   |_  [   ]     _]|   /
                                                         LL\/   ,' '--'-'-----'  \  ( 
                                                         ||     ;      |          |  >
                                                         JJ     |      |\         |,/
                                                          JJ    /_     ||       ;_|
                                                           LL   L "==='|i======='_|
                                                            ||    i----' '-------';
                                                             JJ    ';-----.------,-'
                                                             LL     L_.__J,'---;'
                                                              ||      |   ,|    (
                                                               JJ     .'=  (|  ,_|
                                                                LL   /    .'L_    \ 
                                                                ||   '---'    '.___>


                """


elf = """

                                                                ███████╗██╗     ███████╗
                                                                ██╔════╝██║     ██╔════╝
                                                                █████╗  ██║     █████╗  
                                                                ██╔══╝  ██║     ██╔══╝  
                                                                ███████╗███████╗██║     
                                                                ╚══════╝╚══════╝╚═╝     
                                                                                    
                                                                      .;;,.
                                                                     ; '" ;\ \//
                                                                    \|a (a|7 \//
                                                                    j| ..  | ||/
                                                                    //'.--.')\-,/
                                                                .-||- '' ||/  `-.
                                                                ;  | \ |/ |/ L.  ,|
                                                                f\ |\| Y  || \ '._\ 
                                                                j | \|     (| |   | |
                                                                \(  '-.,-,    |   ; |
                                                                |'-.'.L_rr>  f--f  |
                                                    .-=,,______,--------- J-. ;  ;__ 
                                                    ``"-,__     |  |      h  |  f    '--.__
                                                            `--;;--,_       h  f-j   |   __;==-.
                                                                / `-''-,,__J,'  \_..--:'-'     '
                                                                | |    `' --L7//'-'`|
                                                                | ,     ||  h    |  (
                                                                | ;     | \ J    j   |
                                                                | L__   | |  L_.'    |
                                                                |   |'-.| L.'h  |  : |
                                                                |;  \     |  J ; : : :|
                                                                    : \     \  'L| : : |
                                                                        \   \   |'L_j
                                                                        _>  _|   |
                                                                    <___/ /-  \ 
                                                                            /    /
                                                                            '---' 

                """
                                #

def start_menu_structure():
    menu = [wizzard, knight, rouge, dwarf, elf]
    # 88
    instruction = "TO NAVIGATE USE 'A'- KEY TO MOVE LEFT OR 'D' KEY TO MOVE RIGHT"
    title = choose_character

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
    if key == 'c':
        output = move_forward(option)
    num_of_option = handle_menu_option(option)  
    return [output, num_of_option]


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
        print(wizzard)
        input()
        return wizzard
        pass
    elif where == 1:
        helpers.clear_screen()
        print(knight)
        input()
        return knight
        pass
    elif where == 2:
        helpers.clear_screen()
        print(rouge)
        input()
        return rouge
        pass
    elif where == 3:
        helpers.clear_screen()
        print(dwarf)
        input()
        return dwarf
        pass
    elif where == 4:
        helpers.clear_screen()
        print(elf)
        input()
        return elf
        pass
    elif where == 9:
        # go to LEAVE
        output = False
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
        
