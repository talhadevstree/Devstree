#Create Animal base class with Dog and Cat subclasses demonstrating inheritance

class Animal:
    def sound(self):
        print('\n')
        print("This is Animal Base class")
class Dog(Animal):
    def bark(self):
        print("Dog Barks!!")
class Cat(Animal):
    def meow(self):
        print("Cat can Meoww!!")
     
obj1 = Dog()
obj2 = Cat()

obj1.sound()
obj1.bark()

obj2.sound()
obj2.meow()
