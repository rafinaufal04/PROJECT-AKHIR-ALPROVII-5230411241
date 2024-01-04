import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

jenis = 'Mamalia'
cursor.execute(f"DELETE FROM HEWAN WHERE jenis = '(jenis)'")

conn.commit()
conn.close()