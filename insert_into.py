import sqlite3
koneksi = sqlite3.connect('database_hewan.db')

koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Orangutan', 'Mamalia', 'Sumatera', '14000', '2021')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Harimau Sumatera', 'Mamalia', 'Sumatera', '400', '2020')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Komodo', 'Repril', 'Nusa Tenggara', '3000', '2019')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Anoa', 'Mamalia', 'Sulawesi', '5000', '2022')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Badak Jawa', 'Mamalia', 'Jawa', '72', '2021')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Kuskus', 'Mamamia', 'Papua', '50', '2020')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Trenggiling', 'Mamalia', 'Sumatera', '90', '2020')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Burung Cendrawasih', 'Burung', 'Papua', '45', '2022')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Penyu Hijau', 'Repril', 'Nusa Tenggara Timur', '20', '2022')")
koneksi.execute("INSERT INTO HEWAN (nama, jenis, asal, jml_skrg, thn_ditemukan) VALUES ('Gajah Sumatera', 'Mamalia', 'Sumatera', '2500', '2023')")
koneksi.commit()

koneksi.close()