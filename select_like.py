import sqlite3
 
conn = sqlite3.connect('database_hewan.db')
kursor = conn.cursor()
 
print("nama hewan yang diawali dengan karakter “B”:")
kursor.execute("select * from HEWAN WHERE nama LIKE 'B%'")
 
rows = kursor.fetchall()
 
print("==========================================================================================================")
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Sekarang", "Tahun Ditemukan"))
print("----------------------------------------------------------------------------------------------------------")
for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4],  row[5]))