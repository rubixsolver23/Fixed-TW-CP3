

class DessertItem:
    def __init__(self, name):
        self.name = name

class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        
class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

class Order:
    def __init__(self):
        self.order = []
    
    def add(self, item):
        self.order.append(item)
        return self
    
    def __len__(self):
        return len(self.order)
    

def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    order1.add(Candy("Gummy Bears", .25, .35))
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    order1.add(IceCream("Pistachio", 2, .79))
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in order1.order:
        print(item.name)
    
    print(f"Total number of items in order: {len(order1)}")

main()