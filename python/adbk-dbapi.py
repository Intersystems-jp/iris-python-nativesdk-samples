import iris

def main():
  connection_string = "localhost:1972/USER"
  username = "_system"
  password = "SYS"

  connection = iris.connect(connection_string, username, password)
  cursor = connection.cursor()

  try:
    sql = "Select * from Samples.ADBK where id = ?"
    params = [1]
    cursor.execute(sql, params) 
    cursor.fetchall
    rows = cursor.fetchall()

    for row in rows:
      print(row)

  except Exception as ex:
    print(ex)
  finally:
    if cursor:
      cursor.close()
    if connection:
      connection.close()

if __name__ == "__main__":
  main()