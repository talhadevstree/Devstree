#Implement Shape base class with Circle, Rectangle, and Triangle subclasses

class Shape:
    def base(self):
        print("This is a Base or Parent Class")

class Circle(Shape):
    def sub(self):
        print("This is a circle!!")
class Rectangle(Shape):
    def sub1(self):
        print("This is Rectangle!!")
class Triangle(Shape):
    def sub2(self):
        print("This is a Trianle!!")

obj1 = Shape()
obj1.base()


obj2 = Circle()
obj2.base()
obj2.sub()

obj3 = Rectangle()
obj3.base()
obj3.sub1()

obj4 = Triangle()
obj4.base()
obj4.sub2()

