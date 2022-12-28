import os
import pandas as pd

import connection

cursor = connection.db.cursor()

# USE ONLY TO RESET
# 
cursor.execute("DROP DATABASE IF EXISTS " + connection.database)
# 

cursor.execute("CREATE DATABASE IF NOT EXISTS " + connection.database)
cursor.execute("USE " + connection.database)

for x in os.listdir('data'):
  tableName = x.split('.')[0]
  data = pd.read_csv(f'data/{x}')
  df = pd.DataFrame(data)
  tableFields = df.columns
  numFields = len(df.columns)
  typeSQL = ""
  stringSQL = ""
  stringValPlaceholder = ""
  row_inc = 1
  
  for y in range(len(tableFields)):

    if y == len(tableFields) - 1:
      stringSQL += f"{tableFields[y]} "
    else:
      stringSQL += f"{tableFields[y]}, "

    if y == len(tableFields) - 1:
      stringValPlaceholder += "%s"
    else:
      stringValPlaceholder += "%s,"

    if df.dtypes[y] == "int64":
      if y == len(tableFields) - 1:  
        typeSQL += f"{tableFields[y]} INT"
      else:
        typeSQL += f"{tableFields[y]} INT, "

    elif df.dtypes[y] == "float64":
      if y == len(tableFields) - 1: 
        typeSQL += f"{tableFields[y]} DECIMAL"
      else:
        typeSQL += f"{tableFields[y]} DECIMAL, "
      
    elif df.dtypes[y] == "object":
      if y == len(tableFields) - 1:
        typeSQL += f"{tableFields[y]} VARCHAR(1000)"
      else:
        typeSQL += f"{tableFields[y]} VARCHAR(1000), "

  cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tableName} ({typeSQL})''')
  for row in df.itertuples():
    preval = []
    for x in range(1, len(row)):
      preval.append((row[x]))
    val = tuple(preval)
    print(val)
    sql = (f'''INSERT INTO {tableName} ({stringSQL}) VALUES ({stringValPlaceholder})''')  
    cursor.execute(sql,val)   

connection.db.commit()
cursor.close()
connection.db.close()

print("\nDatabase seeded.\n")