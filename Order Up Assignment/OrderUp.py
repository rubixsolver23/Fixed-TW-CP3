import sys

def sanitize(string):
    string_list = string.split()
    for idx, word in enumerate(string_list):
        string_list[idx] = word.lower().capitalize()
    return " ".join(string_list)

class Order:
    menu = None
    def __init__(self):
        self.drink = self.get_drink()
        self.appetizer = self.get_appetizer()
        self.main_course = self.get_main_course()
        self.sides = self.get_sides()
        self.dessert = self.get_dessert()
        self.price = None
    
    def get_drink(self):
        order = None
        while order not in menu["Drink"]:
            order = sanitize(input("What would you like to drink?: "))
            if order == "Nothing":
                break
            if order not in menu["Drink"]:
                print("This is not on the menu.")
        return order
    
    def get_appetizer(self):
        order = None
        while order not in menu["Appetizer"]:
            order = sanitize(input("What would you like for an appetizer?: "))
            if order == "Nothing":
                break
            if order not in menu["Appetizer"]:
                print("This is not on the menu.")
        return order
    
    def get_main_course(self):
        order = None
        while order not in menu["Main Course"]:
            order = sanitize(input("What would you like for your main course?: "))
            if order == "Nothing":
                break
            if order not in menu["Main Course"]:
                print("This is not on the menu.")
        return order
    
    def get_sides(self):
        order = None
        while order not in menu["Sides"]:
            order = sanitize(input("What would you like for a side?: "))
            if order == "Nothing":
                break
            if order not in menu["Sides"]:
                print("This is not on the menu.")
        if order == "Nothing":
            return ["Nothing", "Nothing"]
        else:
            order = [order]
            order2 = None
            while order2 not in menu["Sides"]:
                order2 = sanitize(input("What would you like for another side?: "))
                if order2 == "Nothing":
                    order.append("Nothing")
                    return order
                if order2 not in menu["Sides"]:
                    print("This is not on the menu.")
            order.append(order2)
            return order
    
    def get_dessert(self):
        order = None
        while order not in menu["Dessert"]:
            order = sanitize(input("What would you like for your dessert?: "))
            if order == "Nothing":
                break
            if order not in menu["Dessert"]:
                print("This is not on the menu.")
        return order

    def __str__(self):
        return f"You have ordered: {self.drink} to drink, {self.appetizer} for your appetizer, {self.main_course} for your main course, {self.sides[0]} for one side, {self.sides[1]} for your second side and {self.dessert} for dessert."
    
    def calculate_price(self):
        if self.drink == "Nothing":
            d_price = 0.00
        else:
            d_price = menu["Drink"][self.drink]

        if self.appetizer == "Nothing":
            a_price = 0.00
        else:
            a_price = menu["Appetizer"][self.appetizer]

        if self.main_course == "Nothing":
            m_price = 0.00
        else:
            m_price = menu["Main Course"][self.main_course]
        
        if self.sides[0] == "Nothing":
            s_price = 0.00
        else:
            if self.sides[1] == "Nothing":
                s_price = menu["Sides"][self.sides[0]]
            else:
                s_price = menu["Sides"][self.sides[0]] + menu["Sides"][self.sides[1]]
        
        if self.dessert == "Nothing":
            de_price = 0.00
        else:
            de_price = menu["Dessert"][self.dessert]

        return f"${(d_price + a_price + m_price + s_price + de_price):.2f}"
    
    @classmethod
    def print_menu(self):
        print("Here is our menu:")
        for heading in menu.keys():
            print("\n"+heading)
            for item in menu[heading].keys():
                print(f"{item} for ${menu[heading][item]:.2f}")


    @staticmethod
    def check_if_blank(object):
        if object.drink == "Nothing" and object.appetizer == "Nothing" and object.main_course == "Nothing" and object.sides == ["Nothing", "Nothing"] and object.dessert == "Nothing":
            return True


menu = {

"Drink": {
"Water": 0.00,
"Soft Drink (s)": 1.50,
"Soft Drink (m)": 2.00,
"Soft Drink (l)": 3.00,
"Chocolate Milk": 2.50},


"Appetizer": {
"Garlic Bread": 4.00,
"Buttered Toast": 3.00,
"Onion Rings": 3.00},

"Main Course": {
"Ribeye Steak": 25.00,
"Hamburger": 15.00,
"Hot Dog": 10.00,
"Macoroni & Cheese": 10.00,
"Tomato Soup": 20.00,
"Shrimp & Prime Rib": 35.00},

"Sides": {
"French Fries": 2.00,
"Salad": 4.00,
"Scones": 3.00,
"Chips & Salsa": 5.00,
"Mixed Fruit": 2.00,
"Watermelon Slices": 2.50},

"Dessert": {
"Soft Serve Cone": 1.50,
"Chocolate Cake": 5.00,
"Ice Cream Sundae": 4.00,
"Brownies": 2.50,
"Oreo Milkshake": 4.50}
}

Order.menu = menu
Order.print_menu()

my_meal = Order()

if Order.check_if_blank(my_meal):
    print("If you won't order someting, we're going to have to ask you to leave.")
    my_meal = Order()
    if Order.check_if_blank(my_meal):
        print("We're going to have to kick you out now.")
        sys.exit()
    else:
        pass


print(my_meal)
print("Total:", my_meal.calculate_price())
change_part = sanitize(input("Would you like to change some part of your order? (y/n): "))
while change_part == "Y":
    part_to_change = None
    while part_to_change not in Order.menu.keys():
        part_to_change = sanitize(input("What part would you like to change? (Drink, Appetizer, Main Course, Sides, Dessert): "))
        if part_to_change not in Order.menu.keys():
            print("This is not a valid option.")
        else:
            if part_to_change == "Drink":
                my_meal.drink = my_meal.get_drink()
            elif part_to_change == "Appetizer":
                my_meal.appetizer = my_meal.get_appetizer()
            elif part_to_change == "Main Course":
                my_meal.main_course = my_meal.get_main_course()
            elif part_to_change == "Sides":
                my_meal.sides = my_meal.get_sides()
            elif part_to_change == "Dessert":
                my_meal.dessert = my_meal.get_dessert()

    print(my_meal)
    print("Total:", my_meal.calculate_price())
    change_part = sanitize(input("Would you like to change some part of your order? (y/n): "))

print(f"Your total is {my_meal.calculate_price()}. Enjoy your meal!")