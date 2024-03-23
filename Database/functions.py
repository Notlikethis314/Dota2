import json

def drop_table(cursor, table_name):
    """
    Drop a table from the database.
    cursor: db cursor object.
    table_name: name of the table to be dropped.
    """
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

def create_table(cursor, table_name, columns):
    """
    Create a new table in the database.
    cursor: db cursor object.
    table_name: name of the table to be created.
    columns: a dictionary with column names as keys and SQLite data types as values.
    """
    columns_with_types = ', '.join([f'{col} {type}' for col, type in columns.items()])
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})')

def insert_into_table(cursor, table_name, data):
    """
    Insert new data into the table.
    cursor: db cursor object.
    table_name: name of the table to insert data into.
    data: a dictionary with column names as keys and the corresponding data as values.
    """
    data = {k: json.dumps(v) if isinstance(v, (list, dict)) else v for k, v in data.items()}
    columns = ', '.join(data.keys())
    placeholders = ', '.join('%s' for _ in data)
    cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})', tuple(data.values()))
