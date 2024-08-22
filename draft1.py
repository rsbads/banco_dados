import pandas as pd
import sqlite3

from functions.create_db import create_db
from functions.drop_table import drop_table

create_db('mydatabase')

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INT ,
        nome STR
)
               
""")

cursor.execute("""
    DROP TABLE cliente
""")
