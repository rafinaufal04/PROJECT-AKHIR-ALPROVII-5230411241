import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

cursor.execute("SELECT SUM(jml_skrg) FROM HEWAN")
total_hewan = cursor.fetchone()[0]

print(f"Total Populasi Hewan Langka Saat Ini: {total_hewan}")

conn.close()
