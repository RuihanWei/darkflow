#!/usr/bin/python
import MySQLdb
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")