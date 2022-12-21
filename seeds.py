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

categoriesData = pd.read_csv (r'data/categories.csv')
customersData = pd.read_csv (r'data/customers.csv')   
employee_territoriesData = pd.read_csv (r'data/employee_territories.csv')
employeesData = pd.read_csv (r'data/employees.csv')
order_detailsData = pd.read_csv (r'data/order_details.csv')
ordersData = pd.read_csv (r'data/orders.csv')   
productsData = pd.read_csv (r'data/products.csv')
regionsData = pd.read_csv (r'data/regions.csv')
shippersData = pd.read_csv (r'data/shippers.csv')
suppliersData = pd.read_csv (r'data/suppliers.csv')   
territoriesData = pd.read_csv (r'data/territories.csv')

categories_df = pd.DataFrame(categoriesData)
customers_df = pd.DataFrame(customersData)
employee_territories_df = pd.DataFrame(employee_territoriesData)
employees_df = pd.DataFrame(employeesData)
order_details_df = pd.DataFrame(order_detailsData)
orders_df = pd.DataFrame(ordersData)
products_df = pd.DataFrame(productsData)
regions_df = pd.DataFrame(regionsData)
shippers_df = pd.DataFrame(shippersData)
suppliers_df = pd.DataFrame(suppliersData)
territories_df = pd.DataFrame(territoriesData)

cursor = db.cursor()

# USE ONLY TO RESET
# 
# cursor.execute("DROP DATABASE IF EXISTS " + database)
# 

cursor.execute("CREATE DATABASE IF NOT EXISTS " + database)
cursor.execute("USE " + database)

cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
    categoryID INT AUTO_INCREMENT PRIMARY KEY,
    categoryName VARCHAR(255),
    description VARCHAR(255),
    picture VARCHAR(1000))''')

for row in categories_df.itertuples():
    sql=('''
        INSERT INTO categories (
            categoryID,
            categoryName,
            description,
            picture)
        VALUES (%s,%s,%s,%s)
        ''')

    val = (
        row.categoryID,
        row.categoryName,
        row.description,
        row.picture)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
    customerID VARCHAR(255),
    companyName VARCHAR(255),
    contactName VARCHAR(255),
    contactTitle VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    postalCode VARCHAR(255),
    country VARCHAR(255),
    phone VARCHAR(255),
    fax VARCHAR(255))''')

for row in customers_df.itertuples():
    sql=('''
        INSERT INTO customers (
            customerID,
            companyName,
            contactName,
            contactTitle,
            address,
            city,
            region,
            postalCode,
            country,
            phone,
            fax)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')

    val = (
        row.customerID,
        row.companyName,
        row.contactName,
        row.contactTitle,
        row.address,
        row.city,
        row.region,
        row.postalCode,
        row.country,
        row.phone,
        row.fax)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS employee_territories (
    employeeID INT,
    territoryID INT)''')

for row in employee_territories_df.itertuples():
    sql=('''
        INSERT INTO employee_territories (
            employeeID,
            territoryID)
        VALUES (%s,%s)
        ''')

    val = (
        row.employeeID,
        row.territoryID)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    employeeID  INT AUTO_INCREMENT PRIMARY KEY,
    lastName VARCHAR(255),
    firstName VARCHAR(255),
    title VARCHAR(255),
    titleOfCourtesy VARCHAR(255),
    birthDate DATETIME,
    hireDate DATETIME,
    address VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    postalCode VARCHAR(255),
    homePhone VARCHAR(255),
    extension VARCHAR(255),
    photo VARCHAR(1000),
    notes VARCHAR(255),
    reportsTo INT,
    photoPath VARCHAR(1000))''')

for row in employees_df.itertuples():
    sql=('''
        INSERT INTO employees (
            employeeID,
            lastName,
            firstName,
            title,
            titleOfCourtesy,
            birthDate,
            hireDate,
            address,
            city,
            region,
            postalCode,
            homePhone,
            extension,
            photo,
            notes,
            reportsTo,
            photoPath)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')

    val = (
        row.employeeID,
        row.lastName,
        row.firstName,
        row.title,
        row.titleOfCourtesy,
        row.birthDate,
        row.hireDate,
        row.address,
        row.city,
        row.region,
        row.postalCode,
        row.homePhone,
        row.extension,
        row.photo,
        row.notes,
        row.reportsTo,
        row.photoPath)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS order_details (
    orderID INT,
    productID INT,
    unitPrice DECIMAL,
    quantity INT,
    discount DECIMAL)''')

for row in order_details_df.itertuples():
    sql=('''
        INSERT INTO order_details (
            orderID,
            productID,
            unitPrice,
            quantity,
            discount)
        VALUES (%s,%s,%s,%s,%s)
        ''')

    val = (
        row.orderID,
        row.productID,
        row.unitPrice,
        row.quantity,
        row.discount)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    orderID INT,
    customerID VARCHAR(255),
    employeeID VARCHAR(255),
    orderDate DATETIME,
    requiredDate DATETIME,
    shippedDate DATETIME,
    shipVia INT,
    freight DECIMAL,
    shipName VARCHAR(255),
    shipAddress VARCHAR(255),
    shipCity VARCHAR(255),
    shipRegion VARCHAR(255),
    shipPostalCode VARCHAR(255),
    shipCountry VARCHAR(255))''')

for row in orders_df.itertuples():
    sql=('''
        INSERT INTO orders (
            orderID,
            customerID,
            employeeID,
            orderDate,
            requiredDate,
            shippedDate,
            shipVia,
            freight,
            shipName,
            shipAddress,
            shipCity,
            shipRegion,
            shipPostalCode,
            shipCountry)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')

    val = (
        row.orderID,
        row.customerID,
        row.employeeID,
        row.orderDate,
        row.requiredDate,
        row.shippedDate,
        row.shipVia,
        row.freight,
        row.shipName,
        row.shipAddress,
        row.shipCity,
        row.shipRegion,
        row.shipPostalCode,
        row.shipCountry)
    
    cursor.execute(sql,val)

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

for row in products_df.itertuples():
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

cursor.execute('''CREATE TABLE IF NOT EXISTS regions (
    regionID INT AUTO_INCREMENT PRIMARY KEY,
    regionDescription VARCHAR(255))''')

for row in regions_df.itertuples():
    sql=('''
        INSERT INTO regions (
            regionID,
            regionDescription)
        VALUES (%s,%s)
        ''')

    val = (
        row.regionID,
        row.regionDescription)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS shippers (
    shipperID INT AUTO_INCREMENT PRIMARY KEY,
    companyName VARCHAR(255),
    phone VARCHAR(255))''')

for row in shippers_df.itertuples():
    sql=('''
        INSERT INTO shippers (
            shipperID,
            companyName,
            phone)
        VALUES (%s,%s,%s)
        ''')

    val = (
        row.shipperID,
        row.companyName,
        row.phone)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers (
    supplierID INT AUTO_INCREMENT PRIMARY KEY,
    companyName VARCHAR(255),
    contactName VARCHAR(255),
    contactTitle VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    postalCode VARCHAR(255),
    country VARCHAR(255),
    phone VARCHAR(255),
    fax VARCHAR(255),
    homePage VARCHAR(255))''')

for row in suppliers_df.itertuples():
    sql=('''
        INSERT INTO suppliers (
            supplierID,
            companyName,
            contactName,
            contactTitle,
            address,
            city,
            region,
            postalCode,
            country,
            phone,
            fax,
            homePage)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''')

    val = (
        row.supplierID,
        row.companyName,
        row.contactName,
        row.contactTitle,
        row.address,
        row.city,
        row.region,
        row.postalCode,
        row.country,
        row.phone,
        row.fax,
        row.homePage)
    
    cursor.execute(sql,val)

cursor.execute('''CREATE TABLE IF NOT EXISTS territories (
    territoryID INT AUTO_INCREMENT PRIMARY KEY,
    territoryDescription VARCHAR(255),
    regionID INT)''')

for row in territories_df.itertuples():
    sql=('''
        INSERT INTO territories (
            territoryID,
            territoryDescription,
            regionID)
        VALUES (%s,%s,%s)
        ''')

    val = (
        row.territoryID,
        row.territoryDescription,
        row.regionID)
    
    cursor.execute(sql,val)

db.commit()

print("\nDatabase seeded.\n")
