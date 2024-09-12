import sqlite3

def insert_one_row(
    database_name: str,
    table_name: str,
    columns_name: str,
    values: tuple
) -> None:
    """
    Inserts a single row into a specified SQLite table.

    Parameters:
    - database_name (str): The name of the SQLite database (without the .db extension).
    - table_name (str): The name of the table where the row will be inserted.
    - columns_name (str): A comma-separated string of column names where the values will be inserted.
    - values (tuple): A tuple containing the values to be inserted into the columns.

    Returns:
    - None: This function does not return a value.

    Example:
    >>> insert_one_row(
    ...     database_name='my_database',
    ...     table_name='my_table',
    ...     columns_name='name, age, email',
    ...     values=('John Doe', 30, 'john.doe@example.com')
    ... )
    """
    
    database_name = f'{database_name}.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the SQL query with placeholders
    placeholders = ', '.join('?' * len(values))
    query = f"""
        INSERT INTO {table_name} ({columns_name})
        VALUES ({placeholders})
    """
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return None
