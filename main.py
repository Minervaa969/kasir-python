from utils import *

daftar_barang = load_data()

while True:
  print("\n◖◖◖◖◖ SISTEM KASIR ◗◗◗◗◗\n")
  print("1. Input Barang")
  print("2. Tampilkan Barang")
  print("3. Cari Barang")
  print("4. Update Barang")
  print("5. Hapus Barang")
  print("6. Transaksi")
  print("7. Keluar")
  pilih = input("\nPilih menu (1-7) : ")

  if pilih == "1":
    menu_input(daftar_barang)

  elif pilih == "2":
    menu_tampil(daftar_barang)

  elif pilih == "3":
    menu_cari(daftar_barang)

  elif pilih == "4":
    menu_update(daftar_barang)

  elif pilih == "5":
    menu_hapus(daftar_barang)

  elif pilih == "6":
    menu_transaksi(daftar_barang)

  elif pilih == "7":
    print("Terima kasih telah menggunakan sistem kasir ini")
    break

  else:
    print("Pilihan tidak valid")