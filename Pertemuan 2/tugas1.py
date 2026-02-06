# ========================================================== 
# TUGAS PRAKTIKUM HARI KE-2
# Studi Kasus: Sistem Stok Barang Toko Buah (Berbasis File .txt) 
# ========================================================== 
# Nama  : Muhamad De Almas Dhoifurohman
# NIM   : J0403251013
# Kelas : TPL B2
# ==========================================================

NAMA_FILE = "stok_barang.txt"                                           # Nama file penyimpanan data stok barang

# ==========================================================
# MEMBACA DATA DARI FILE KE DICTIONARY
# ==========================================================
def load_stok(nama_file):
    stok_barang = {}                                                    # dictionary untuk menyimpan data stok

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:                                                # pastikan baris tidak kosong
                    kode, nama, stok = baris.split(",")
                    stok_barang[kode] = {
                        "nama": nama,
                        "stok": int(stok)
                    }
    except FileNotFoundError:
        print("File belum ada. File akan dibuat saat data disimpan nanti.")

    return stok_barang

# ==========================================================
# MENAMPILKAN SEMUA STOK BARANG
# ==========================================================
def tampilkan_semua_barang(stok_barang):
    if len(stok_barang) == 0:                                           # mengecek apakah dictionary kosong
        print("Stok barang masih kosong.")
        return

    print("\n============= DAFTAR STOK BARANG =============")           # menampilkan dalam bentuk tabel
    print(f"{'KODE':<10} | {'NAMA BARANG':<20} | {'STOK':>5}")
    print("-" * 45)

    for kode in sorted(stok_barang.keys()):
        nama = stok_barang[kode]["nama"]
        stok = stok_barang[kode]["stok"]
        print(f"{kode:<10} | {nama:<20} | {stok:>5}")

# ==========================================================
# MENCARI BARANG BERDASARKAN KODE
# ==========================================================
def cari_barang(stok_barang):
    # input kode barang yang ingin dicari
    kode_cari = input("Masukkan kode barang: ").strip().upper()

    if kode_cari in stok_barang:                                    # mengecek apakah kode ada di dictionary
        data = stok_barang[kode_cari]
        print("\n===== BARANG DITEMUKAN =====")                     # menampilkan detail barang jika ditemukan
        print(f"KODE : {kode_cari}")
        print(f"NAMA : {data['nama']}")
        print(f"STOK : {data['stok']}")
    else:
        print("Barang tidak ditemukan.")                            # Jika kode tidak ada di dictionary

# ==========================================================
# MENAMBAH BARANG BARU
# ==========================================================
def tambah_barang(stok_barang):
    print("\n===== TAMBAH BARANG =====")
    
    kode = input("Masukkan kode barang: ").strip().upper()          # input kode barang

    if kode in stok_barang:                                         # cek apakah kode sudah ada
        print("Kode sudah ada! Gagal menambah barang.")
        return

    nama = input("Masukkan nama barang: ").strip()                  # input nama barang

    try:
        stok = int(input("Masukkan jumlah stok: ").strip())         # input stok 
        if stok < 0:                                                # mencegah stok menjadi negatif
            print("Stok tidak boleh negatif!")
            return
    except ValueError:                                              # error handling
        print("Stok harus berupa angka!")
        return

    stok_barang[kode] = {"nama": nama, "stok": stok}                # simpan ke dictionary

    print("\nBarang berhasil ditambahkan!")                         # tampilkan pesan sukses
    print(f"KODE : {kode}")
    print(f"NAMA : {nama}")
    print(f"STOK : {stok}")

# ==========================================================
# UPDATE STOK BARANG
# ==========================================================
def update_stok(stok_barang):

    kode = input("Masukkan kode barang: ").strip().upper()          # input kode barang

    if kode not in stok_barang:                                     # cek apakah kode ada
        print("Kode tidak ditemukan.")
        return

    while True:                                                     # operasi benar salah
        print("\n1. Tambah stok")                                   # menambahkan stok
        print("2. Kurangi stok")                                    # mengurangi stok
        pilihan = input("Pilih (1/2): ").strip()

        if pilihan in ["1", "2"]:
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())            # input jumlah perubahan stok
        if jumlah < 0:
            print("Jumlah tidak boleh negatif!")
            return
    except ValueError:                                              # error handling
        print("Jumlah harus berupa angka!")
        return

    stok_lama = stok_barang[kode]["stok"]                           # menentukan stok lama

    if pilihan == "1":                                              # proses update stok
        stok_baru = stok_lama + jumlah
    else:
        stok_baru = stok_lama - jumlah
        if stok_baru < 0:
            print("Stok tidak boleh kurang dari 0!")
            return

    stok_barang[kode]["stok"] = stok_baru                           # simpan stok baru

    print(f"Stok berhasil diupdate: {stok_lama} -> {stok_baru}")

# ==========================================================
# MENYIMPAN DATA KE FILE
# ==========================================================
def simpan_stok(nama_file, stok_barang):
    with open(nama_file, "w", encoding="utf-8") as file:                    # membuka file dalam mode tulis ("w")
        for kode in sorted(stok_barang.keys()):                             # menulis data satu per satu ke file
            nama = stok_barang[kode]["nama"]
            stok = stok_barang[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

    print("Data berhasil disimpan!")

# ==========================================================
# FUNGSI UTAMA (MENU PROGRAM)
# ==========================================================
def main():

    stok_barang = load_stok(NAMA_FILE)                              # load data saat program dijalankan

    while True:
        print("\n===== SISTEM STOK KANTIN =====")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok")
        print("5. Simpan data")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()                         # menu program

        if pilihan == "1":
            tampilkan_semua_barang(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)

        elif pilihan == "0":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":                                     # menjalankan program utama
    main()
