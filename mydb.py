#pip install mysql
#pip install pymysql

import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="4444",
    database="ISM_DB"
)

cursor = dataBase.cursor()


print("Database Connected Successfully!")
