import ui

end_screen = {
    "die": ['''
    ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████  ▐██▌ 
     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀  ▐██▌ 
      ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███    ▐██▌ 
      ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄  ▓██▒ 
      ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒ ▒▄▄  
       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ░▀▀▒ 
     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░  ░ 
     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░       ░ 
     ░ ░         ░ ░     ░           ░     ░     ░  ░ ░    
     ░ ░                           ░                       
    ''', "You misunderstood the power of rats. The big Rat-necromancer defeated you, your flesh fed his offspring.\nThe last thing you saw was a young woman standing beside the Necromancer."],
    "win": ['''
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
                                                             
    ''', "The Skeleton-rats was crowding in on you, but you gather all your strength and with the last stroke\nfinally you defeat the big Rat-necromancer! All undead monsters turn into ashes and Giant-rars spread out.\n\nYou see the young woman. You are so glad that such a beauty wasn't killed.\nYou start to imagine her as your wife...\nBut, what the...\n\nThe woman starts to cry and hugs the Necromancer! You suspect that she isn't grateful for rescue.\nShe yell at you that they loved each other for a long time and finally she deciced to leave her\nfamily. Of course she didn't say a thing to her relatives, because no-one would understand her love.\nHer last words are: 'I will take revenge on you!'\n\nYou see that the dying Necromancer gives some amulet to the woman and BOOOM! She disappears!"]}


def end_game(end):
    title = 0
    end_story = 1
    if end == "die":
        ui.display_ascii(end_screen["die"][title])
        ui.display_dialog_window(end_screen["die"][end_story])
    elif end == "win":
        ui.display_ascii(end_screen["win"][title])
        ui.display_dialog_window(end_screen["win"][end_story])
