#!/usr/bin/python
import MySQLdb
import mysql.connector


#cursor.execute("CREATE TABLE objects (id INT AUTO_INCREMENT PRIMARY KEY, label VARCHAR(255), confidence FLOAT)")
# cursor.execute("CREATE DATABASE ObjectVC")


class ObjectVcConnector:
  def __init__(self):
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="rienwave1",
      database = "ObjectVC"
    )

  def insert(self, label, confidence):
    cursor = db.cursor()
    sql = "INSERT INTO objects (label, confidence) VALUES (%s, %s)"
    val = (label, confidence)
    cursor.execute(sql, val)
