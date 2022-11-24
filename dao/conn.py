import sqlite3
conn = None

def getConn():
  global conn
  if(conn is None):
    conn = sqlite3.connect("weather.db")
  return conn
