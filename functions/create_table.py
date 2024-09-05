import sqlite3

def create_table(
    database: str,
    table_name: str,
    columns_desc: str
) -> None:
    """
    Creates a table in an SQLite database if it does not already exist.

    This function connects to the specified SQLite database and creates a new
    table with the given name and column description. If the table already exists,
    the function does nothing.

    Parameters:
    - database (str): The name of the database, without the '.db' extension. The database
      will be created if it does not exist.
    - table_name (str): The name of the table to be created.
    - columns_desc (str): A string describing the columns and their data types,
      in the format expected by the SQL `CREATE TABLE` command. For example,
      "id_cliente INT PRIMARY KEY, nome TEXT".

    Returns:
    - None: This function does not return any value. It only creates the table in the database.

    Example:
    >>> create_table('mydatabase', 'client', 'id_cliente INT PRIMARY KEY, nome TEXT')
    """
    
    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns_desc})""")

    conn.close()
