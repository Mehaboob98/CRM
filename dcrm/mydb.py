import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mehaboob3698'
)

#prepare a cursor
cursorObject= dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print('all done')