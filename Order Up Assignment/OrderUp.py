

class Order:
    def __init__(self, menu, drink, appetizer, main_course, dessert, sides=[]):
        self.menu = menu
        self.drink = drink
        self.appetizer = appetizer
        self.main_course = main_course
        self.sides = sides
        self.dessert = dessert

    
    
    def __str__(self):
        return f"You have ordered: {self.drink}, {self.appetizer}, {self.main_course}, {self.sides[0]}, {self.sides[1]} and {self.dessert}"




