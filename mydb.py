import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="password"
)

#prepare cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")