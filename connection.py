import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
database = os.environ.get('DBNAME')

db = mysql.connector.connect(
  host= os.environ.get('HOST'),
  user= os.environ.get('USER'),
  password= os.environ.get('PASSWORD'),
)