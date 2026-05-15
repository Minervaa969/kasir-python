import json
from models import Barang

def cek_data(data):
    if not data:
        print("Barang Tidak Ada")
        return False
    return True

def menu_input(data):
    try:
        nama = input("\nMasukan nama barang : ")
        if Barang.cari_barang(data, nama):
            print("Barang Ini Sudah Ada!")
            return
        harga = int(input("Masukan harga barang : "))
        stok = int(input("Masukan stok barang : "))
        data.append(Barang(nama, harga, stok))
        save_data(data)
        print("Barang Ditambahkan!")
    except ValueError:
        print("Input Harus Angka!")

def menu_tampil(data):
    if not cek_data(data):
        return
    print("\nDaftar Barang")
    for b in data:
      print(b)

def menu_cari(data):
    if not cek_data(data):
        return
    nama = input("\nMasukan nama barang : ")
    barang = Barang.cari_barang(data, nama)
    if barang:
        print("\nBarang Ditemukan")
        print(barang)
    else:
        print("\nBarang Tidak Ditemukan")

def menu_update(data):
    if not cek_data(data):
        return
    try:
        nama = input("\nMasukan nama barang : ")
        barang = Barang.cari_barang(data, nama)
        if barang:
            print(barang)
            print("\nPilih data yang ingin diubah \n1. Harga \n2. Stok")
            update = input("Pilih : ")
            if update == "1":
                harga_baru = int(input("Masukan harga baru : "))
                barang.harga = harga_baru
                save_data(data)
                print("Update Berhasil")

            elif update == "2":
                stok_baru = int(input("Masukan stok baru : "))
                barang.stok = stok_baru
                save_data(data)
                print("Update Berhasil")

            else:
                print("Pilihan tidak valid")
        else:
            print("\nBarang tidak ditemukan")
    except ValueError:
        print("Input Harus Angka!")

def menu_hapus(data):
    if not cek_data(data):
        return
    nama = input("\nMasukan nama barang : ")
    barang = Barang.cari_barang(data, nama)
    if barang:
        print(barang)
        konfir = input("Yakin ingin menghapus data barang ini? (y/n) : ")
        if konfir.lower() == "y":
            data.remove(barang)
            save_data(data)
            print("Barang Berhasil Dihapus")
    else:
        print("\nBarang tidak ditemukan")

def menu_transaksi(data):
    if not cek_data(data):
        return
    try:
        jumlah = int(input("Masukan jumlah jenis barang: "))

        keranjang = []
        total_semua = 0
        for i in range(jumlah):
            nama = input("\nNama barang: ")
            jumlah_beli = int(input("Jumlah beli: "))
            barang = Barang.cari_barang(data, nama)

            if not barang:
                print("Barang tidak ditemukan")
                continue
          
            if jumlah_beli > barang.stok:
                print("Stok tidak cukup")
                return

            total = barang.harga * jumlah_beli
            print(f"Total harga : {total}")
            keranjang.append((barang, jumlah_beli))
            total_semua += total
        print(f"\nTotal belanja : {total_semua}")
    
        uang = int(input("\nMasukan uang : "))
        if uang < total_semua:
            print("Uang tidak cukup")
            return

        for barang, jumlah_beli in keranjang:
            barang.stok -= jumlah_beli

        kembalian = uang - total_semua
        print(f"Kembalian : {kembalian}")
        save_data(data)

        print("\nTransaksi Berhasil")
        print("Terima kasih telah berbelanja")
    except ValueError:
        print("Input Harus Angka!")

def save_data(data):
    with open("daftar_barang.json", "w") as file:
        json.dump([s.to_d() for s in data], file, indent=4)

def load_data():
    try:
        with open("daftar_barang.json", "r") as file:
            data_json = json.load(file)
            return [
                Barang(i["nama"], i["harga"], i["stok"])
                for i in data_json
            ]
    except (FileNotFoundError, json.JSONDecodeError):
        return []