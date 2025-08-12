# Read and write CSV files with student data, calculate averages
import csv

with open('file/student.csv', 'a') as f:
     f.write("Name,Math,Science,English\n")
     f.write("Ali,85,90,78\n")
     f.write("Sara,92,88,84\n")
     f.write("John,75,80,70\n")
     f.write("Aisha,89,94,91\n")
  

with open ('file/student.csv' ,'r') as r:
    content = csv.reader(r)
    next(content)
    for row in content:
        name = row[0].strip()
        math = int(row[1].strip())
        science = int(row[2].strip())
        english = int(row[3].strip())

        avg = (math + science + english) / 3  
        print(f"{name}'s Average is: {avg:.2f}")




