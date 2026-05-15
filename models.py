class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"\nNama : {self.nama} \nHarga: {self.harga} \nStok: {self.stok}"
    
    def to_d(self):
        return {
            "nama" : self.nama,
            "harga" : self.harga,
            "stok" : self.stok
        }

    @classmethod
    def cari_barang(cls, data, nama):
        for barang in data:
            if barang.nama.lower() == nama.lower():
                return barang
        return None