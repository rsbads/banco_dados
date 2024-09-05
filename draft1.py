import pandas as pd
import sqlite3

from functions.create_db import create_db
from functions.drop_table import drop_table
from functions.create_table import create_table

create_db('mydatabase')

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
   CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INT PRIMARY KEY ,
        nome TEXT
               
""")

columns_desc = """id_cliente INT PRIMARY KEY ,
        nome TEXT"""

create_table(
    database='mydatabase',
    table_name='cliente',
    columns_desc = columns_desc
)

drop_table(
    database='mydatabase',
    table_name='cliente'
)
cursor.execute("""
    DROP TABLE cliente
""")
