import sqlite3
from functions.create_table import create_table
from functions.insert_row import insert_one_row

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Cria a tabela produto
create_table(
    database='mydatabase',
    table_name='produto',
    columns_desc=""" 
        id_produto INTEGER PRIMARY KEY,
        nome CHAR NOT NULL,
        qtd INTEGER NOT NULL
"""
)

# Insere dados na tabela produto
cursor.execute("""
    INSERT INTO produto (nome, qtd)
    VALUES (?, ?)
""", ("PS5", 30))

cursor.execute("""
    INSERT INTO produto (nome, qtd)
    VALUES (?, ?)
""", ("PS4", 20))

# Commit e fechamento da conexão
conn.commit()
conn.close()

# Insere mais uma linha usando a função insert_one_row
insert_one_row(
    database_name='mydatabase',
    table_name='produto',
    columns_name='nome, qtd',
    values=('nintendo switch', 50)
)
