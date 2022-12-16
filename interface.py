import mysql.connector
import os
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv()

db = mysql.connector.connect(
  host= os.environ.get('HOST'),
  user= os.environ.get('USER'),
  password= os.environ.get('PASSWORD'),
)

cursor = db.cursor(buffered=True)

cursor.execute("USE northwindtestingdb")

def init():
    print("\nWelcome to the database! Choose from the options below:\n")
    dataInputQuestion = (input(
'''
1. Add new product (all fields required)
2. Delete product by ID number
3. Search products by first letter
4. Search products by full name
'''))

    if dataInputQuestion == "1":
        productName = input("Product name: ")
        supplierID = int(input("Supplier ID: "))
        categoryID = int(input("Category ID: "))
        quantityPerUnit = int(input("Quantity per unit: "))
        unitPrice = float(input("Price: "))
        unitsInStock = int(input("In stock: "))
        unitsOnOrder = int(input("On order: "))
        reorderLevel = int(input("Reorder level: "))
        discontinued = input("Discontinued (y/n): ")
        sql = '''
            INSERT INTO products (
                productName, 
                supplierID, 
                categoryID, 
                quantityPerUnit, 
                unitPrice, 
                unitsInStock, 
                unitsOnOrder, 
                reorderLevel, 
                discontinued) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

        val = (
            productName, 
            supplierID, 
            categoryID, 
            quantityPerUnit, 
            unitPrice, 
            unitsInStock, 
            unitsOnOrder, 
            reorderLevel, 
            discontinued
            )

        cursor.execute(sql, val)
        db.commit()
        print("\nProduct '" + productName + "' added.\n")

    elif dataInputQuestion == "2":
        productID = input("Enter product ID: ")
        cursor.execute("DELETE FROM products WHERE productID = " + productID)
        db.commit()
        print("\nProduct " + productID + " deleted.\n")

    elif dataInputQuestion == "3":
        def checkInput():
            firstLetter = input("Enter first letter: ")
            if len(firstLetter) > 1:
                checkInput()

        firstLetter = input("Enter first letter: ")
        if len(firstLetter) > 1:
            checkInput()

        cursor.execute("SELECT productID, productName, unitPrice, unitsInStock FROM products WHERE productName LIKE '" + firstLetter + "%'")
        db.commit()

        result = cursor.fetchall()
        print("\n Results:")
        print(tabulate(result, headers=['productID', 'productName', 'unitPrice', 'unitsInStock'], tablefmt='psql'))

    elif dataInputQuestion == "4":
        productName = input("Enter product name: ").strip().replace("'","''")
        cursor.execute("SELECT productID, productName, unitPrice, unitsInStock FROM products WHERE productName LIKE '%" + productName + "%'")
        db.commit()

        result = cursor.fetchall()
        print("\n Results:")
        print(tabulate(result, headers=['productID', 'productName', 'unitPrice', 'unitsInStock'], tablefmt='psql'))

    else:
        init()

init()
