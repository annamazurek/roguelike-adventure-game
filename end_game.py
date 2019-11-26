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
    ''', '''
You misunderstood the power of rats. The big Rat-necromancer defeated you, your flesh fed his offspring. 
The last thing you saw was a young woman standing beside the Necromancer.
    '''],
    "win": ['''
    __   __                          _         _ 
    \ \ / /                         (_)       | |
     \ V /   ___   _   _  __      __ _  _ __  | |
      \ /   / _ \ | | | | \ \ /\ / /| || '_ \ | |
      | |  | (_) || |_| |  \ V  V / | || | | ||_|
      \_/   \___/  \__,_|   \_/\_/  |_||_| |_|(_)

    ''', '''
The Skeleton-rats was crowding in on you, but you gather all your strength and with the last stroke finally you defeat
the big Rat-necromancer! All undead monsters turn into ashes and Giant-rars spread out.

You see the young woman. You are so glad that such a beauty wasn't killed. You start to imagine her as your wife... 
But, what the...
The woman starts to cry and hugs the Necromancer! You suspect that she isn't grateful for rescue. She yell at you that
they loved each other for a long time and finally she deciced to leave her family. Of course she didn't say a thing
to her relatives, because no-one would understand her love. Her last words are:
"I will take revenge on you!"

You see that the dying Necromancer gives some amulet to the woman and BOOOM! She disappears!


    ''']}


def end_game(end):
    title = 0
    end_story = 1
    if end == "die":
        ui.display_ascii(end_screen["die"][title])
        ui.display_ascii(end_screen["die"][end_story])
    elif end == "win":
        ui.display_ascii(end_screen["win"][title])
        ui.display_ascii(end_screen["win"][end_story])
