import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()
SERVER = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

"""SimpleConnection"""
connectionString = f'''DRIVER={{SQL Server}};
                       SERVER={SERVER};
                       DATABASE={DATABASE};
                       Trusted_Connections=yes'''
# "CREATE DB Params"
# SQL_QUERY = r"""
# CREATE DATABASE Products
# ON
# (
# NAME = Products_database_data,
# FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Products_database_data.mdf',
# SIZE = 10MB,
# MAXSIZE = 10 GB,
# FILEGROWTH=5%)"""


# SQL_QUERY = """
# CREATE TABLE products_table
# (product_id int PRIMARY KEY,
# product_name nvarchar(50),
# price int);
# """


# SQL_QUERY = """
# INSERT INTO products_table (product_id, product_name, price)
# VALUES
# (1, 'Desktop Computer', 800),
# (2, 'Laptop', 1200),
# (3, 'Tablet', 200),
# (4, 'Monitor', 350),
# (5, 'Printer', 150)"""


SQL_QUERY = """
SELECT *
FROM products_table"""

conn = pyodbc.connect(connectionString)
conn.autocommit = True
cursor = conn.cursor()
try:
    cursor.execute("USE Products")
    cursor.execute(SQL_QUERY)
except pyodbc.Error as ex:
    print(ex)
else:
    records = cursor.fetchall()
    for record in records:
        print(f"{record.product_id}\t{record.product_name}\t{record.price}")
finally:
    conn.close()

