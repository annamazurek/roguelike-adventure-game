class Hero:

    # def __init__(self, name, sex, race, hero_class, character, health, mana, strength, dexterity, constitution, intelligence, wisdom, charisma):

    def __init__(self, name, sex, race, hero_class, character):
        self.name = name
        self.sex = sex
        self.race = race
        self.hero_class = hero_class
        self.character = character


hero = Hero(
    "Janusz",
    "M",
    "Human",
    "Warrior",
    "N",
)

setattr(hero, "race", "Ogr")
print(getattr(hero, "race"))