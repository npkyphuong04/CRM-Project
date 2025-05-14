# pip install pymysql
# pip install mysqlclient
# Run command: "python mydb.py" in terminal to test the connection

import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="4444",
    database="ISM_DB"
)

cursor = dataBase.cursor()

# Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS ISM_DB")

print("Database Connected Successfully!")