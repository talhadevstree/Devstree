# Design a Student class with properties and methods for grade management

class Student:
    def __init__(self , name):
        self.name = name
        self.grades = []
    def add_grades(self , grade):
        self.grades.append(grade)
        print(f"Grade Added")
    def avg_grade(self):
        if self.grades:
            avg = sum(self.grades) / len (self.grades)
            print(f"{avg:.0f} average Grade")
    def display_grade(self):
        if self.grades:
            print(f"{self.name} has this Grade ==>{self.grades}")
g = Student("John")
grade1 = int(input("Enter grade:"))
grade2 = int(input("Enter grade:"))
g.add_grades(grade1 and grade2)
g.avg_grade()
g.display_grade()

