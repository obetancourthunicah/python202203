from dao.conn import getConn

class weather_dao():
  conn = None
  cursor = None

  def __init__(self):
    self.conn = getConn()
    self.cursor = self.conn.cursor()
    table_weather_create_sql = "CREATE TABLE IF NOT EXISTS WEATHER (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, country STRING, tz_id STRING, region STRING, lat REAL, lon REAL);"
    self.cursor.execute(table_weather_create_sql)
    self.conn.commit()

  def addOne(self, name, country, tz_id, region, lat, log):
    insert_sql = "INSERT INTO WEATHER (name, country, tz_id, region, lat, lon) values (?, ?, ?, ?, ?, ?);"
    self.cursor.execute(insert_sql, (name, country, tz_id, region, lat, log))
    self.conn.commit()
  def getAll(self):
    select_sql = "SELECT * from WEATHER;"
    self.cursor.execute(select_sql)
    return self.cursor.fetchall()
