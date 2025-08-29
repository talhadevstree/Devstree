import sqlite3

def create_table():
    connection = sqlite3.connect("myexpense.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE if not exists expense
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                income REAL ,
                expense REAL,
                balance REAL,
                transcation TEXT)
                """
    )

    connection.commit()
    connection.close()  