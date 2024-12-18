# polymorphism functions or methods can do multiple different things based on given inputs
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def area(self):
        return 0
    

class Square(Shape):

    def area(self):
        return self.x ** 2
    
class Circle(Shape):

    def area(self):
        return round(self.x ** 2 * math.pi, 2)

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    
    def area(self):
        return self.x * self.y
    

shapes = [Square(4), Circle(4), Rectangle(3,5), "cheese", "bacon", "stellated octahedron"]

for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())




