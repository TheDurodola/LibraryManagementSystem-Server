import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Durodola62"
)

my_cursor = mydb.cursor()


my_cursor.execute("CREATE DATABASE IF NOT EXISTS library")

my_cursor.execute("SHOW DATABASES")
databases = my_cursor.fetchall()


my_cursor.close()
mydb.close()


