#Create Car and Dealership classes with inventory management

class Car:
    def __init__(self , name , model , year, price ):
        self.name = name
        self.model = model
        self.year = year
        self.price = price

    def car_info(self):
        return f"{self.name}  {self.model}  {self.year} {self.price}"

class Dealership:
    def __init__(self , name ):
            self.name = name
            self.inventory = []
    def add_car(self , name , model , year , price):
         car = Car(name , model , year , price)
         self.inventory.append(car)
         print("Inventory  Added")
         print('\n')

    def display(self):
        if self.inventory:
            print(f"---------Inventory of {self.name}-----------")
            for car in self.inventory:
                print(car.car_info())
            print(f"----------------Thanks You----------------")
        else:
            print('\n')
            print("Inventory is empty")
    
carn = input("Car Name :")
carm = input("Car Model :")
cary =input("Car Year :")
carp =input("Car Price :")

obj2 = Dealership("Autoworld")

obj2.add_car(carn , carm , cary , carp)
obj2.display()