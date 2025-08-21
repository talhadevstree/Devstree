# Implement Create, Read, Update, Delete operations for database records
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE if not exists studentinfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT,
        rollno INTEGER NOT NULL,
        branch TEXT NOT NULL)"""
)
while True:
    choice = input(
        "Which operation do you want to perform: 1. Insert 2. Read 3. Update 4. Delete 5. Exit"
    )

    if choice == "1":
        name = input("Enter the name of student:")
        course = input("Enter the course of student:")
        rollno = input("Enter the rollno of student:")
        branch = input("Enter the branch of student:")
        cursor.execute(
            "INSERT INTO studentinfo (name , course , rollno, branch) VALUES (? , ? , ? , ?)",
            (name, course, rollno, branch),
        )
        print("Student Added in a Database")
        connection.commit()

    elif choice == "2":
        if cursor.execute("SELECT * FROM studentinfo"):
            for data in cursor.fetchall():
                print(data)
        else:
            print("No Data Found")

    elif choice == "3":
        uname = input("Enter name of student want to update:")
        cursor.execute("SELECT * from studentinfo WHERE name = ?", (uname,))
        student = cursor.fetchone()

        if student:
                print(f"Which Thing Want to update for {uname}")
                print("1. Update Name:")
                print("2. Update course:")
                print("3. Update rollno:")
                print("4. Update branch:")
                choice = input("Enter your operation:")

                if choice == "1":
                    updatename = input("Enter your new name to update:")
                    cursor.execute(
                        "UPDATE studentinfo SET name = ? WHERE name= ?",
                        (updatename, uname),
                    )
                    print("Name updated Successfully !")
                    connection.commit()
                    

                elif choice == "2":
                    updatecourse = input("Enter your new course to update:")
                    cursor.execute(
                        "UPDATE studentinfo SET course = ?  WHERE name= ? ",
                        (updatecourse, uname),
                    )
                    print("Course update successfully!")
                    connection.commit()
                    

                elif choice == "3":
                    updaterollno = input("Enter your new rollno to update:")
                    cursor.execute(
                        "UPDATE studentinfo SET rollno = ?  WHERE name= ? ",
                        (updaterollno, uname),
                    )
                    print("Rollno update successfully!")
                    connection.commit()
                    

                elif choice == "4":
                    updatebranch = input("Enter your new branch update:")
                    cursor.execute(
                        "UPDATE studentinfo SET branch = ?  WHERE name= ? ",
                        (updatebranch, uname),
                    )
                    print("branch update successfully!")
                    connection.commit()

                else:
                    print("Invalid operator!")
        else:
                print("No Student Found")

    elif choice == "4":
        delname = input("Enter name to delete")

        cursor.execute("DELETE from studentinfo WHERE name  = ?", (delname,))
        connection.commit()
        
        if cursor.rowcount>0:
            print("Row Deleted")
        else:
            print("No Row Found")

    elif choice == "5":
        print("Exiting!")
        break

    else:
        print("Invalid operator")

connection.commit()
connection.close()
