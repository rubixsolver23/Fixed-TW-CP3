

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
        while order not in menu:
            order = input("What would you like to drink?: ")
            if order == "nothing":
                break
            if order not in menu:
                print("This is not on the menu.")
        return order
    
    def get_appetizer(self):
        order = None
        while order not in menu:
            order = input("What would you like for an appetizer?: ")
            if order == "nothing":
                break
            if order not in menu:
                print("This is not on the menu.")
        return order
    
    def get_main_course(self):
        order = None
        while order not in menu:
            order = input("What would you like for your main course?: ")
            if order == "nothing":
                break
            if order not in menu:
                print("This is not on the menu.")
        return order
    
    def get_sides(self):
        order = None
        while order not in menu:
            order = input("What would you like for a side?: ")
            if order == "nothing":
                break
            if order not in menu:
                print("This is not on the menu.")
        if order == "nothing":
            return order
        else:
            order = [order]
            order2 = None
            while order2 not in menu:
                order2 = input("What would you like for another side?: ")
                if order == "nothing":
                    return order
                if order2 not in menu:
                    print("This is not on the menu.")
            order.append(order2)
            return order
    
    def get_dessert(self):
        order = None
        while order not in menu:
            order = input("What would you like for your dessert?: ")
            if order == "nothing":
                break
            if order not in menu:
                print("This is not on the menu.")
        return order

    def __str__(self):
        return f"You have ordered: {self.drink}, {self.appetizer}, {self.main_course}, {self.sides[0]}, \
            {self.sides[1]} and {self.dessert}"
    
    def calculate_price(self):
        return menu[self.drink] + menu[self.appetizer] + menu[self.main_course] + \
            menu[self.sides[0]] + menu[self.sides[1]] + menu[self.dessert]
    @classmethod
    def print_menu(self):
        print("Here is our menu:")
        for item in menu.keys():

            if "heading" in item:
                print("\n" + menu[item])
            else:
                print(f"{item} for ${menu[item]:.2f}")

    @staticmethod
    def check_if_blank(object):
        if object.drink == "nothing" and object.appetizer == "nothing" and object.main_course == "nothing" and \
            object.sides == "nothing" and object.dessert == "nothing":
            return True


menu = {

"heading1": "Drinks",
"Water": 0.00,
"Soft Drink (s)": 1.50,
"Soft Drink (m)": 2.00,
"Soft Drink (l)": 3.00,
"Chocolate Milk": 2.50,

"heading2": "Appetizers",
"Garlic Bread": 4.00,
"Buttered Toast": 3.00,
"Onion Rings": 3.00,

"heading3": "Main Courses",
"Ribeye Steak": 25.00,
"Hamburger": 15.00,
"Hot Dog": 10.00,
"Macoroni & Cheese": 10.00,
"Tomato Soup": 20.00,
"Shrimp & Prime Rib": 35.00,

"heading4": "Sides",
"French Fries": 2.00,
"Salad": 4.00,
"Scones": 3.00,
"Chips & Salsa": 5.00,
"Mixed Fruit": 2.00,
"Watermelon Slices": 2.50,

"heading5": "Desserts",
"Soft Serve Cone": 1.50,
"Chocolate Cake": 5.00,
"Ice Cream Sundae": 4.00,
"Brownies": 2.50,
"Oreo Milkshake": 4.50
}

Order.menu = menu
Order.print_menu()

my_meal = Order()