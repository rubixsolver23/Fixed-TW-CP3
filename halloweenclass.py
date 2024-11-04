import random
import time

class Monster:
    def __init__(self, name, where_from, health):
        self.name = name
        self.where_from = where_from
        self.health = health

    def attack(self):
        pass

    def get_defense(self):
        return random.randint(0, 10) + self.defense
    
    def get_offense(self):
        return random.randint(0, 10) + self.offense

class Bush(Monster):
    def __init__(self, name, where_from):
        super().__init__(name, where_from, 10)
        self.defense = 5
        self.offense = 2


    def attack(self, other):
        print(self.name, "uses leaf-dash!")
        time.sleep(.8)
        if issubclass(other.__class__, Monster):
            if other.get_defense() > self.get_offense():
                print(self.name, "overshot the dash!")
                return False
            else:
                print(self.name, "knocked over", other.name)
                other.health -= 1
                return True
        else:
            return "NO"
        
class Sand(Monster):
    def __init__(self, name, where_from):
        super().__init__(name, where_from, 12)
        self.defense = 2
        self.offense = -1


    def attack(self, other):
        print(self.name, "uses sand-blast!")
        time.sleep(.8)
        if issubclass(other.__class__, Monster):
            other.defense -= 1
            print(self.name, "wore down", other.name + "'s defenses!")
            if other.get_defense() > self.get_offense():
                time.sleep(.5)
                print(self.name, "missed!")
                return False
            else:
                time.sleep(.5)
                print(self.name, "wore down", other.name + "'s health!")
                other.health -= 1
                return True
        else:
            return "NO"

class Trash(Monster):
    def __init__(self, name, where_from):
        super().__init__(name, where_from, 10)
        self.defense = 4
        self.offense = 2


    def attack(self, other):
        print(self.name, "uses engulf!")
        time.sleep(.8)
        if issubclass(other.__class__, Monster):
            if other.get_defense() > self.get_offense():
                print(self.name, "couldn't catch", other.name)
                return False
            else:
                print(self.name, "successfully engulfed", other.name, "in garbage!")
                other.health -= 1
                return True
        else:
            return "NO"

class Box(Monster):
    def __init__(self, name, where_from):
        super().__init__(name, where_from, 1)
        self.defense = 999
        self.offense = 0

    def get_offense(self):
        if random.randint(0, 5) == 0:
            return 10000
        else:
            return -200

    def attack(self, other):
        print(self.name, "uses sit!")
        time.sleep(3)
        if issubclass(other.__class__, Monster):
            if other.get_defense() > self.get_offense():
                print("Nothing happened!")
                return False
            else:
                print(self.name, "spontaniously exploded!!!")
                self.health = 0
                other.health = 0
                return True
        else:
            return "NO"


def battle(monster1, monster2):
    print("A battle is starting between", monster1.name, "from", monster1.where_from, "and", monster2.name, "from", monster2.where_from + "!")
    print(monster1.name, "will go first! Let the battle begin!")
    time.sleep(1)
    while monster1.health > 0 and monster2.health > 0:
        monster1.attack(monster2)
        time.sleep(.8)
        if monster2.health <= 0:
            break
        
        monster2.attack(monster1)
        time.sleep(.8)
    if monster1.health <= 0 and monster2.health <= 0:
        print("Both monsters died!")
        return False
    elif monster1.health <= 0:
        print(monster2.name, "wins!")
        return 2
    elif monster2.health <= 0:
        print(monster2.name, "wins!")
        return 1


bush = Bush("Harry", "Downtown")
sand = Sand("Vortex", "Moab")
trash = Trash("Carl", "Egypt")
box = Box("dn ʎɐʍ sᴉɥ┴", "Amazon")

bracket = [bush, sand, trash, box]
random.shuffle(bracket)

battle1 = battle(bracket[0], bracket[1])
if battle1:
    if battle1 == 1:
        bracket.pop[1]
    else:
        bracket.pop[0]
    battle2 = battle(bracket[1], bracket[2])
else:
    bracket.pop[0]
    bracket.pop[1]
    battle2 = battle(bracket[0], bracket[1])

