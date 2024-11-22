from datetime import datetime

class Parkir:
    def __init__(self):
        self.kendaraan = {}
        self.tarif_per_jam = 5000  # Tarif parkir per jam

    def kendaraan_masuk(self, plat_nomor):
        """Mencatat kendaraan yang masuk ke area parkir."""
        waktu_masuk = datetime.now()
        self.kendaraan[plat_nomor] = waktu_masuk
        print(f"Kendaraan dengan plat nomor {plat_nomor} masuk pada {waktu_masuk.strftime('%Y-%m-%d %H:%M:%S')}.")

    def kendaraan_keluar(self, plat_nomor):
        """Mencatat kendaraan yang keluar dan menghitung biaya parkir."""
        if plat_nomor not in self.kendaraan:
            print(f"Kendaraan dengan plat nomor {plat_nomor} tidak terdaftar di parkir.")
            return
        
        waktu_keluar = datetime.now()
        waktu_masuk = self.kendaraan[plat_nomor]
        lama_parkir = (waktu_keluar - waktu_masuk).total_seconds() / 3600  # Menghitung lama parkir dalam jam
        biaya_parkir = round(lama_parkir * self.tarif_per_jam, 2)
        
        print(f"Kendaraan dengan plat nomor {plat_nomor} keluar pada {waktu_keluar.strftime('%Y-%m-%d %H:%M:%S')}.")
        print(f"Lama parkir: {round(lama_parkir, 2)} jam.")
        print(f"Total biaya parkir: Rp {biaya_parkir}")
        
        # Menghapus kendaraan dari daftar parkir
        del self.kendaraan[plat_nomor]

    def total_kendaraan_parkir(self):
        """Menampilkan jumlah kendaraan yang masih parkir."""
        print(f"Jumlah kendaraan yang masih parkir: {len(self.kendaraan)}")

    def pendapatan_total(self):
        """Menghitung total pendapatan dari parkir."""
        total = 0
        for waktu_masuk in self.kendaraan.values():
            # Asumsikan semua kendaraan masih parkir, kita hitung lama parkir sampai saat ini
            lama_parkir = (datetime.now() - waktu_masuk).total_seconds() / 3600
            total += lama_parkir * self.tarif_per_jam
        print(f"Total pendapatan parkir saat ini: Rp {round(total, 2)}")


# Contoh penggunaan
parkir = Parkir()

# Kendaraan masuk
parkir.kendaraan_masuk("B1234XYZ")
parkir.kendaraan_masuk("A9876BCD")

# Menunggu beberapa saat (simulasi)
import time
time.sleep(5)  # Simulasi 5 detik untuk parkir

# Kendaraan keluar
parkir.kendaraan_keluar("B1234XYZ")

# Kendaraan lain masuk dan keluar
time.sleep(3)
parkir.kendaraan_keluar("A9876BCD")

# Menampilkan data
parkir.total_kendaraan_parkir()
parkir.pendapatan_total()
