import os
from tabulate import tabulate

import connection
import pandasfuns
import plots

cursor = connection.db.cursor(buffered=True)

cursor.execute("USE " + connection.database)

print("\nWelcome to the database! Choose from the options below:")

def init():
    mainMenu = (input(
'''
1. List all tables
2. View table
3. Alter products table
4. Query products data
5. Plots menu
'''))

# Create new table
# Alter table
# Delete table
# Drop database

    if mainMenu == "1":
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()
        print("\n Tables in " + connection.database + ":")
        print(tabulate(result, tablefmt='psql'))
        init()
    elif mainMenu == "2":
        chooseTable = (input("Enter table name: "))
        cursor.execute("SELECT * FROM " + chooseTable)
        init()
    elif mainMenu == "3":
        alterProducts()
    elif mainMenu == "4":
        pandasFuns()
    elif mainMenu == "5":
        plotsDisplay()
    else:
        init()

def alterProducts():
    dataInputQuestion = (input(
'''
1. Add new product (all fields required)
2. Delete product by ID number
3. Search products by first letter
4. Search products by full name
5. Back to main menu
'''))

    if dataInputQuestion == "1":
        productID = input("Product ID: ")
        productName = input("Product name: ")
        supplierID = int(input("Supplier ID: "))
        categoryID = int(input("Category ID: "))
        quantityPerUnit = int(input("Quantity per unit: "))
        unitPrice = float(input("Price: "))
        unitsInStock = int(input("In stock: "))
        unitsOnOrder = int(input("On order: "))
        reorderLevel = int(input("Reorder level: "))
        discontinued = (input("Discontinued (y/n): "))

        def checkInput():
            discontinued = (input("Discontinued (y/n): "))
            if discontinued == "y":
                discontinued = 0
            elif discontinued == "n":
                discontinued = 1
            else:
                checkInput()
    
        if discontinued == "y":
            discontinued = 0
        elif discontinued == "n":
            discontinued = 1
        else:
            checkInput()
        
        sql = '''
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
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

        val = (
            productID,
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
        connection.db.commit()
        print("\nProduct '" + productName + "' added.\n")
        alterProducts()

    elif dataInputQuestion == "2":
        productID = input("Enter product ID: ")
        cursor.execute("DELETE FROM products WHERE productID = " + productID)
        connection.db.commit()
        print("\nProduct " + productID + " deleted.\n")
        alterProducts()

    elif dataInputQuestion == "3":
        def checkInput():
            firstLetter = input("Enter first letter: ")
            if len(firstLetter) > 1:
                checkInput()

        firstLetter = input("Enter first letter: ")
        if len(firstLetter) > 1:
            checkInput()

        cursor.execute("SELECT productID, productName, unitPrice, unitsInStock FROM products WHERE productName LIKE '" + firstLetter + "%'")
        connection.db.commit()

        result = cursor.fetchall()
        print("\n Results:")
        print(tabulate(result, headers=['productID', 'productName', 'unitPrice', 'unitsInStock'], tablefmt='psql'))
        alterProducts()

    elif dataInputQuestion == "4":
        productName = input("Enter product name: ").strip().replace("'","''")
        cursor.execute("SELECT productID, productName, unitPrice, unitsInStock FROM products WHERE productName LIKE '%" + productName + "%'")
        connection.db.commit()

        result = cursor.fetchall()
        print("\n Results:")
        print(tabulate(result, headers=['productID', 'productName', 'unitPrice', 'unitsInStock'], tablefmt='psql'))
        alterProducts()
    else:
        init()

def pandasFuns():
    print("Choose what to view: ")
    choosePandas = (input(
'''
1. Description
2. Numeric covariance
3. Numeric sums
4. Back to main menu
'''))
    if choosePandas == "1":
        pandasfuns.description()
    if choosePandas == "2":
        pandasfuns.cov()
    if choosePandas == "3":
        pandasfuns.sum()
    if choosePandas == "4":
        init()
    else:
        pandasFuns()

def plotsDisplay():
    print("Choose type of graph: ")
    graphType = (input(
'''
1. Scatter
2. Bar
3. Back to main menu
'''))
    if graphType == "1":
        graph = "scatter"
    elif graphType == "2":
        graph = "bar"
    elif graphType == "3":
        init()
    else:
        plotsDisplay()

    print("Choose table to display: ")
    plotsMenu = (input(
'''
1. products
2. order_details
3. Back to main menu
'''))
    if plotsMenu == "1":
        fieldMenu = (input(
'''
1. unitsInStock by productID
2. unitsOnOrder by productID
3. Back to choose table
'''))   
        if fieldMenu == "1":
            plots.plotHist("products", graph, "productID", "unitsInStock")
            plotsDisplay()
        elif fieldMenu == "2":
            plots.plotHist("products", graph, "productID", "unitsOnOrder")
            plotsDisplay()
        else:
            plotsDisplay()

    elif plotsMenu == "2":
        fieldMenu = (input(
'''
1. unitPrice by orderID
2. quantity by orderID
3. Back to choose table
'''))
        if fieldMenu == "1":
            plots.plotHist("order_details", graph, "orderID", "unitPrice")
            plotsDisplay()
        elif fieldMenu == "2":
            plots.plotHist("order_details", graph, "orderID", "quantity")
            plotsDisplay()
        else:
            plotsDisplay()

    else:
        init()

init()
