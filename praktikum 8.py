import time

NAMA  = ["MUGI MULIYO PAMBUDI"]
NIM   = ('312510376')
KELAS = ('TI.25.C5')
print('\n')

def display_names():
    print("\n")
    for i, name in enumerate(NAMA,):
        print(f"NAMA: {name}")
        time.sleep(0.9)
        print(f"NIM: {NIM}")
        time.sleep(0.9)
        print(f"KELAS: {KELAS}")
        time.sleep(0.9)
# Jalankan fungsi
display_names()

class Mahasiswa:
    def __init__(self):
        # Data awal
        self.data = {
            "Mugi Muliyo Pambudi": {
                "nim": "312510376",
                "nilai": 90,
                "umur": 23,
                "alamat": "Bekasi"
            }
        }

    def tampilkan(self):
        print("\n=== Daftar Mahasiswa ===")
        if not self.data:
            print("Belum ada data.")
        else:
            for nama, info in self.data.items():
                print(f"\nNama     : {nama}")
                print(f"NIM      : {info['nim']}")
                print(f"Nilai    : {info['nilai']}")
                print(f"Umur     : {info['umur']}")
                print(f"Alamat   : {info['alamat']}")
        print("=========================\n")

    def tambah(self):
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai = int(input("Masukkan nilai: "))
        umur = int(input("Masukkan umur: "))
        alamat = input("Masukkan alamat: ")

        if nama in self.data:
            print("Data dengan nama tersebut sudah ada!")
        else:
            self.data[nama] = {
                "nim": nim,
                "nilai": nilai,
                "umur": umur,
                "alamat": alamat
            }
            print("Data berhasil ditambah!")

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data {nama} berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    def ubah(self, nama):
        if nama in self.data:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            nim = input("NIM baru: ")
            nilai = input("Nilai baru: ")
            umur = input("Umur baru: ")
            alamat = input("Alamat baru: ")

            if nim:
                self.data[nama]["nim"] = nim
            if nilai:
                self.data[nama]["nilai"] = int(nilai)
            if umur:
                self.data[nama]["umur"] = int(umur)
            if alamat:
                self.data[nama]["alamat"] = alamat

            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")


# Program Utama
if __name__ == "__main__":
    daftar = Mahasiswa()

    while True:
        print("\n=== APLIKASI DATA MAHASISWA ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            daftar.tampilkan()
        elif pilihan == "2":
            daftar.tambah()
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin diubah: ")
            daftar.ubah(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang ingin dihapus: ")
            daftar.hapus(nama)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
print("\n✨ Selesai! ✨")