def read_file(filename):
    highscore = []
    with open(filename, 'r') as f:
        for line in f:
            score = line.strip().split(';')
            highscore.append(score)
        return highscore

    # and save to list of list


def sort_score(score_list):
    SCORE_POSITION = 1
    return sorted(score_list, key=lambda h_score: h_score[SCORE_POSITION])

def print_highscore(score_list):
    NAME = 0
    SCORE = 1
    RACE = 2
    CLASS = 3
    print('HALL OF FAME'.center(200,' '))
    for index, player in enumerate(score_list):
        if index <= 9:
            print(f"{index + 1}: {player[NAME]} as {player[RACE]} {player[CLASS]} with {player[SCORE]} points".center(200,' '))
        else:
            pass
    print('Press any key to continue'.center(200,' '))