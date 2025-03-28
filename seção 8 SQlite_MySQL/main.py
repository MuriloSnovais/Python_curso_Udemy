import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where


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

cursor.close()
connection.close()
