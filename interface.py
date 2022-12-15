import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
  host= os.environ.get('HOST'),
  user= os.environ.get('USER'),
  password= os.environ.get('PASSWORD'),
)

cursor = db.cursor()
cursor.execute("USE northwindtestingdb")

def init():
    print("\nWelcome to the database!\n")
    dataInputQuestion = input("Add or delete product? ")

    if dataInputQuestion == "add":
        productName = input("Product name: ")
        supplierID = input("Supplier ID: ")
        categoryID = input("Category ID: ")
        quantityPerUnit = input("Quantity per unit: ")
        unitPrice = input("Price: ")
        unitsInStock = input("In stock: ")
        unitsOnOrder = input("On order: ")
        reorderLevel = input("Reorder level: ")
        discontinued = input("Discontinued (INT): ")
        sql = "INSERT INTO products (productName, supplierID, categoryID, quantityPerUnit, unitPrice, unitsInStock, unitsOnOrder, reorderLevel, discontinued) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (productName, supplierID, categoryID, quantityPerUnit, unitPrice, unitsInStock, unitsOnOrder, reorderLevel, discontinued)
        cursor.execute(sql, val)
        db.commit()
        print("Product '" + productName + "' added.")

    elif dataInputQuestion == "delete":
        productID = input("Enter product ID: ")
        cursor.execute("DELETE FROM products WHERE productID = " + productID)
        db.commit()
        print("Product " + productID + " deleted.")
    else:
        init()

init()
