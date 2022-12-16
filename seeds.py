import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

db = mysql.connector.connect(
  host= os.environ.get('HOST'),
  user= os.environ.get('USER'),
  password= os.environ.get('PASSWORD'),
)

data = pd.read_csv (r'products.csv')   
df = pd.DataFrame(data)

cursor = db.cursor()

# USE ONLY TO RESET
# 
cursor.execute("DROP DATABASE IF EXISTS northwindtestingdb")
# 

cursor.execute("CREATE DATABASE IF NOT EXISTS northwindtestingdb")
cursor.execute("USE northwindtestingdb")

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    productID INT AUTO_INCREMENT PRIMARY KEY,
    productName VARCHAR(255),
    supplierID INT,
    categoryID INT,
    quantityPerUnit VARCHAR(255),
    unitPrice DECIMAL,
    unitsInStock INT,
    unitsOnOrder INT,
    reorderLevel INT,
    discontinued BOOLEAN)''')

for row in df.itertuples():
    sql=('''
        INSERT INTO products (
            productID,
            productName,
            supplierID,
            categoryID,
            quantityPerUnit,
            unitPrice,
            unitsInStock,
            unitsOnOrder,
            reorderLevel,
            discontinued)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')

    val = (
        row.productID,
        row.productName,
        row.supplierID,
        row.categoryID,
        row.quantityPerUnit,
        row.unitPrice,
        row.unitsInStock,
        row.unitsOnOrder,
        row.reorderLevel,
        row.discontinued)
    
    cursor.execute(sql,val)

db.commit()

print("\nProducts database seeded.\n")
