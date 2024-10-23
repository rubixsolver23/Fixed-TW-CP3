
# Start class with keyword, name with PascalCase or UpperCamelCase
class Animal:
    # Create the constructor __init__() which defines all attributes of object being created
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
    
    def get_name(self):
        return self.name
    # Methods are funcitons inside of a class
    # This one takes in another animal and returns the one with a longer name
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) == len(other.name):
            self.losses += 1
            other.losses += 1
            return "Tie"
        else:
            self.losses += 1
            return other.name

    # Makes the object into a more readable string
    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nSpecies: {self.species} \nGender: {self.gender} \nRarity: {self.rarity} \nLosses: {self.losses}"

# Store any object into a variable or dictionary or whatever
cat = Animal("Tom", "cat", 21, "Male", "Common")
frog = Animal("Jarrod", "poison dart frog", 500, "Female", "Rare")


# Calling a method using name of object, dot operator, name of method and then any arguments in parenthases
cat.losses = 0
frog.losses = 0
print(cat.fight(frog))

cat.name = "Tyah-homas"
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)

cat = None
print(cat)