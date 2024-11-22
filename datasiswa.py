class Siswa:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas

    def __str__(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Kelas: {self.kelas}"

class DatabaseSiswa:
    def __init__(self):
        self.siswa_list = []

    def tambah_siswa(self, siswa):
        self.siswa_list.append(siswa)

    def tampilkan_siswa(self):
        if not self.siswa_list:
            print("Tidak ada data siswa.")
        else:
            print("\nDaftar Siswa:")
            for siswa in self.siswa_list:
                print(siswa)

    def edit_siswa(self, nama, umur=None, kelas=None):
        for siswa in self.siswa_list:
            if siswa.nama == nama:
                if umur:
                    siswa.umur = umur
                if kelas:
                    siswa.kelas = kelas
                print(f"Data siswa {nama} berhasil diubah.")
                return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

    def hapus_siswa(self, nama):
        for siswa in self.siswa_list:
            if siswa.nama == nama:
                self.siswa_list.remove(siswa)
                print(f"Data siswa {nama} berhasil dihapus.")
                return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

    def cari_siswa(self, nama):
        for siswa in self.siswa_list:
            if siswa.nama.lower() == nama.lower():
                print(siswa)
                return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

def main():
    db = DatabaseSiswa()

    while True:
        print("\n===== Menu =====")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Edit Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Cari Data Siswa")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            nama = input("Nama Siswa: ")
            umur = input("Umur Siswa: ")
            kelas = input("Kelas Siswa: ")
            siswa = Siswa(nama, umur, kelas)
            db.tambah_siswa(siswa)
            print(f"Data siswa {nama} berhasil ditambahkan.")
        
        elif pilihan == '2':
            db.tampilkan_siswa()

        elif pilihan == '3':
            nama = input("Masukkan nama siswa yang akan diedit: ")
            umur = input("Umur baru (kosongkan jika tidak diubah): ")
            kelas = input("Kelas baru (kosongkan jika tidak diubah): ")
            db.edit_siswa(nama, umur if umur else None, kelas if kelas else None)

        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang akan dihapus: ")
            db.hapus_siswa(nama)

        elif pilihan == '5':
            nama = input("Masukkan nama siswa yang akan dicari: ")
            db.cari_siswa(nama)

        elif pilihan == '6':
            print("Terima kasih, sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

if __name__ == "__main__":
    main()
