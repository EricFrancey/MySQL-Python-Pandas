import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
database = os.environ.get('DBNAME')

db = mysql.connector.connect(
  host= os.environ.get('HOST'),
  user= os.environ.get('USER'),
  password= os.environ.get('PASSWORD'),
)

cursor = db.cursor()

# USE ONLY TO RESET
# 
cursor.execute("DROP DATABASE IF EXISTS " + database)
# 

cursor.execute("CREATE DATABASE IF NOT EXISTS " + database)
cursor.execute("USE " + database)

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

db.commit()
cursor.close()
db.close()

print("\nDatabase seeded.\n")