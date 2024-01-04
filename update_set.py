import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

id_hewan = 1
jml_baru = 900

cursor.execute(f"UPDATE HEWAN SET jml_skrg = {jml_baru} WHERE id_hewan = {id_hewan}")
cursor.execute("UPDATE HEWAN SET asal = 'Nusa Tenggara Timur' WHERE id_hewan = 'Komodo'")

conn.commit()
conn.close()
