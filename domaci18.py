


import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "Mozdabek15",
    database = "python17"
)

if connection.open:
    print("connected")
else:
    print("not connected")


def create_user(con, username, password, age):
    cursor = con.cursor()

    query = "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, age))
    con.commit()

    cursor.close()

create_user(connection,'Toma', 'vrevve', 55)
create_user(connection, 'Stefan', 'vevee', 21)