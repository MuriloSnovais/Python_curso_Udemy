import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create  Read   Update Delete
# SQL -  INSERT  SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(f'DELETE FROM {TABLE_NAME}')

# DELETE mais cuidadoso
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight TEXT'
    ')'
)

connection.commit()

# Registar valores na coluna da tabela

# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight) '
#     'VALUES (NULL,?,?)',
#     ["Muliru", 93]
# )

# cursor.executemany(
#     f'INSERT INTO {TABLE_NAME} (name, weight) '
#     'VALUES (:name,:weight)',
#     (("Muliru", 93),("Ygor", 68))
# )
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name,:weight)'

cursor.execute(sql, {"name":"Murilo", "weight": 93})
cursor.executemany(sql, ({"name":"Murilo", "weight": 93},{"name":"Ygor", "weight": 52},{"name":"Kauan", "weight":71}))

connection.commit()

if __name__ == '__main__':

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id= 1')
    connection.commit()

    cursor.execute(f'UPDATE {TABLE_NAME} SET name="QUALQUER", weight=66.32 WHERE id= 4')
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight) 

    connection.commit()

    cursor.close()
    connection.close()