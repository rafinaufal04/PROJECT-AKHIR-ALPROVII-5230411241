# Mengurutkan nama hewan dari awal alfabet
import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY nama ASC")
baris_table = kursor.fetchall()

print("Data Hewan")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah sekarang", "Tahun Ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

# Mengurutkan hewan dari yang terbanyak

kursor.execute("SELECT * FROM HEWAN ORDER BY jml_skrg DESC")
baris_table = kursor.fetchall()

print("Data Hewan")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah sekarang", "Tahun Ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

# Mengurutkan dari tahun yang terlama

kursor.execute("SELECT * FROM HEWAN ORDER BY thn_ditemukan ASC")
baris_table = kursor.fetchall()

print("Data Hewan")
print("==============================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama", "Jenis", "Asal", "Jumlah sekarang", "Tahun Ditemukan"))
print("--------------------------------------------------------------")
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()