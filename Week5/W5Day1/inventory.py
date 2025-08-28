import sqlite3

connection = sqlite3.connect("myinventory.db")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE if not exists inventory
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        supplier TEXT)"""
)

cursor.executemany(
    "INSERT INTO inventory(item_name , category , quantity , price , supplier) VALUES (? , ? , ? , ? , ?)",
    [
        ("Mouse", "Electronics", 150, 540, "HP"),
        ("shirts", "clothes", 300, 399, "codedecoders"),
        ("bat", "sports", 40, 1000, "puma"),
    ],
)

cursor.execute("SELECT * from inventory")
for row in cursor.fetchall():
    print(row)

cursor.execute('UPDATE inventory SET id = 3 WHERE id=4')

connection.commit()
cursor.close()
