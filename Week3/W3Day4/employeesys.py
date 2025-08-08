#Design Employee hierarchy with different types and polymorphic salary calculation

class Employee:
    def main(self):
        print("This is Employee")

class Manager(Employee):
    def calculate_salary(self , base_salary , bonus):
        M_salary = base_salary + bonus
        print("Manager`s Salary :" , M_salary)
        print('\n')

class Developer(Employee):
    def calculate_salary(self, hour_salary, work_hour):
        D_salary = hour_salary * work_hour
        print("Developer`s Salary :", D_salary)
        print('\n')

class Intern(Employee):
    def calculate_salary(self, I_salary):
        print("Intern`s Salary :",I_salary)
        print('\n')


base_salary = int(input("Enter Base Salary for Manager:"))
bonus = int(input("Enter a bonus for Manager:")) 
obj1 = Manager()
obj1.calculate_salary(base_salary , bonus)


hour_salary = int(input("Enter hour salary for Developer:"))
work_hour = int(input("Enter working hour salary for Developer:"))
obj2 = Developer()
obj2.calculate_salary( hour_salary , work_hour)


I_salary = int(input("Enter Stipend for Intern:"))
obj3 = Intern()
obj3.calculate_salary(I_salary)


