# Tampilkan berdasarkan Asal(Sumatera) dan Jumlah Saat ini lebih dari 
# 500 ekor.

import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM HEWAN WHERE Asal == 'Sumatera' OR jml_skrg >= '' ")
rows = cursor.fetchall()

print("Data Hewan:")
print("=============================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("---------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

conn.close()