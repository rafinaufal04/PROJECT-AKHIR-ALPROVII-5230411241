#  Tampilkan berdasarkan jenis = mamalia saja.

import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN WHERE Jenis == 'Mamalia'")
rows = cursor.fetchall()

print("Data Hewan:")
print("=============================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("---------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))


#  Tampilkan berdasarkan hewan jumlahnya kurang dari sama dengan 1000 ekor saja

cursor.execute("SELECT * FROM HEWAN WHERE jml_skrg <= '1000'")
rows = cursor.fetchall()

print("Data Hewan:")
print("=============================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Ditemukan"))
print("---------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))    

conn.close()


