import math
import random

class Mahasiswa:
    def __init__(self, nama, universitas):
        self.nama = nama
        self.universitas = universitas

    def tampilkan_info(self):
        print(f"Nama          : {self.nama}")
        print(f"Universitas   : {self.universitas}")
        print()

class DaftarMahasiswa:
    def __init__(self):
        self.list_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.list_mahasiswa.append(mahasiswa)

    def tampilkan_semua(self):
        print("Daftar Mahasiswa:")
        for mahasiswa in self.list_mahasiswa:
            mahasiswa.tampilkan_info()

# Membuat objek DaftarMahasiswa
daftar_mahasiswa = DaftarMahasiswa()

# Menambahkan data mahasiswa
daftar_mahasiswa.tambah_mahasiswa(Mahasiswa("Rayhan Gading Andri Purwanto", "Universitas Pembangunan Nasional Veteran Jawa Timur"))
daftar_mahasiswa.tambah_mahasiswa(Mahasiswa("Robert William Hendra Tjutju", "Universitas Padjadjaran"))
daftar_mahasiswa.tambah_mahasiswa(Mahasiswa("Siti Arwiyah", "Universitas Terbuka"))
daftar_mahasiswa.tambah_mahasiswa(Mahasiswa("Wildan Miladji", "Universitas Sangga Buasa"))
daftar_mahasiswa.tambah_mahasiswa(Mahasiswa("Yahya Bachtiar Ivansyah", "Universitas Airlangga"))

# Menampilkan semua data mahasiswa
daftar_mahasiswa.tampilkan_semua()

