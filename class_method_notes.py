

class Pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won"
        elif other.lvl > self.lvl:
            return f"{other.name} defeated you"
        else:
            return f"it's a tie between {self.name} and {other.name}"
        
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp * 1.5)

    def __str__(self):
        return f"{self.name}, a {self.typ} type pokemon, is level {self.lvl} and has {self.hp} health left."
    
    # @classmethod makes it unable to change instance varuables

    @classmethod
    def pikachu(self):
        return Pokemon("Pikachu", 50, "electric", 1)
    
    # @staticmethod does not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5



'''    
eevee = Pokemon("Eevee", 37, "normal", 2)
charizard = Pokemon("Charizard", 389, "fire", 99)
print(eevee)
print(charizard)

print(charizard.lvl_up())
print(charizard)
'''

pika = Pokemon.pikachu()
print(pika)

new_hp = Pokemon.hp_update(pika)
pika.hp = new_hp
print(pika)