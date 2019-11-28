def save_result(name, points, race, hero_class):
    score = f"{name};{points};{race};{hero_class}"
    with open('highscore.txt','w') as f:
        f.write(score)
