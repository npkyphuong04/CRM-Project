# pip install pymysql
# pip install mysqlclient
# Run command: "python mydb.py" in terminal to test the connection

import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="4444",
    database="pizzahut"
)

cursor = dataBase.cursor()

#Create a database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS pizzahut")

print("Database Connected Successfully!")