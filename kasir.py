class Kasir:
    def __init__(self):
        self.items = []
        self.total = 0

    def tambah_barang(self, nama_barang, harga, jumlah):
        item = {
            'nama': nama_barang,
            'harga': harga,
            'jumlah': jumlah,
            'subtotal': harga * jumlah
        }
        self.items.append(item)
        self.total += item['subtotal']
        
    def tampilkan_struk(self):
        print("----- Struk Pembelian -----")
        for item in self.items:
            print(f"{item['nama']} - {item['jumlah']} x {item['harga']} = {item['subtotal']}")
        print(f"Total: {self.total}")
    
    def hitung_diskon(self, persen_diskon):
        diskon = self.total * (persen_diskon / 100)
        return diskon
    
    def hitung_pajak(self, persen_pajak):
        pajak = self.total * (persen_pajak / 100)
        return pajak
    
    def hitung_total_akhir(self, persen_diskon, persen_pajak):
        diskon = self.hitung_diskon(persen_diskon)
        pajak = self.hitung_pajak(persen_pajak)
        total_akhir = self.total - diskon + pajak
        return total_akhir

# Contoh penggunaan program Kasir
kasir = Kasir()

# Menambahkan barang
kasir.tambah_barang('Sepatu', 200000, 2)  # Nama barang, harga per item, jumlah
kasir.tambah_barang('Baju', 150000, 1)
kasir.tambah_barang('Topi', 50000, 3)

# Menampilkan struk
kasir.tampilkan_struk()

# Menghitung diskon dan pajak
persen_diskon = 10  # Diskon 10%
persen_pajak = 5    # Pajak 5%

diskon = kasir.hitung_diskon(persen_diskon)
pajak = kasir.hitung_pajak(persen_pajak)

print(f"Diskon ({persen_diskon}%): -{diskon}")
print(f"Pajak ({persen_pajak}%): +{pajak}")

# Menghitung total akhir setelah diskon dan pajak
total_akhir = kasir.hitung_total_akhir(persen_diskon, persen_pajak)
print(f"Total Akhir: {total_akhir}")
