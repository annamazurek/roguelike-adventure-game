class Hero:

    # def __init__(self, name, sex, race, hero_class, character, health, mana, strength, dexterity, constitution, intelligence, wisdom, charisma):

    def __init__(self, name, race, hero_class, character, max_health, max_mana):
        self.name = name
        self.race = race
        self.hero_class = hero_class
        self.character = character
        self.max_health = max_health
        self.max_mana = max_mana


hero = Hero(
    "Janusz",
    "Human",
    "Warrior",
    "Neutral",
    15,
    10
)
actual_stats = {
    'HP': 10,
    'Mana': 10,
    'STR': 10,
    'DEX': 10,
    'CON': 10,
    'INT': 10,
    'WIS': 10,
    'CHA': 10
}


def list_hero_stats(statistics):
    info = []
    for key in ["name", "race", "hero_class", "character"]:
        info.append(f"{getattr(hero, key)}")
    info.append(f"HP: {statistics['HP']}/{hero.max_health}")
    info.append(f"Mana: {statistics['Mana']}/{hero.max_mana}")
    for key, value in list(statistics.items())[2:]:
        info.append(f"{key}: {value}")
    return info





# setattr(hero, "race", "Ogr")
# print(getattr(hero, "race"))
