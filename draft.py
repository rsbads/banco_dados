import pandas as pd
import sqlite3

# create a data example
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create a connection
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame to a table in the database
data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

# closing the connection
conn.close()


########## 
conn = sqlite3.connect('mydatabase.db')

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""


pd.read_sql_query(query, conn)

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