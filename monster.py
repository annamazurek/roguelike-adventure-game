class Monster:

    def __init__(self, name, health, mana, strength, dexterity, intelligence):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence


giant_rat = Monster(
    "Giant rat",
    5,
    0,
    3,
    5,
    10
)


skeleton = Monster(
    "Skeleton",
    10,
    0,
    8,
    8,
    3
)


necromancer = Monster(
    "Necromancer",
    100,
    100,
    15,
    20,
    22
)

mydict = {"damage": 2}

print(skeleton.name)
print(f'HP = {skeleton.health}')
print(f'STR = {skeleton.strength}')
print()

for key in ["name", "health", "mana", "strength", "dexterity", "intelligence"]:
    print(getattr(giant_rat, key, None))
print()
for key in ["name", "health", "mana", "strength", "dexterity", "intelligence"]:
    print(getattr(skeleton, key, None))
print()
while skeleton.health > 0:
    for key in ["health"]:
        setattr(skeleton, key, skeleton.health-mydict["damage"])
    for key in ["name", "health", "mana", "strength", "dexterity", "intelligence"]:
        print(getattr(skeleton, key, None))