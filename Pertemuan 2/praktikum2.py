#Praktikun 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 1 : Membuat fungsi load
#========================================= 

nama_file = "data_mahasiswa.txt"


def baca_data_mahasiswa(nama_file):
    data_dict = {} #buat variabel untuk dictionary

    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
                #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {
                "nama":nama,
                "nilai": int(nilai)
        }
    return(data_dict)

#memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca", len(buka_data))


#========================================= 
#Praktikun 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 2 : Membuat fungsi menampilkan data
#========================================= 


def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print('Data kosong')
        return
    #membuat header tabel
    print("\n==== Daftar Mahasiswa ====")
    print(f"{'NIM' : <10} |{'NAMA' : <12} | {'Nilai' :>5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim : <10} |{nama : <12} | {nilai :>5}")

#tampilkan_data(buka_data)


#========================================= 
#Praktikun 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 3 : Membuat fungsi mencari data
#========================================= 

def cari_data(data_dict):

    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n======= Data Mahasiswa Ditemukan=========")
        print(f'NIM   :{nim_cari}')
        print(f'Nama  :{nama}')
        print(f"NIlai :{nilai}")
    else:
        print('Data tidak ditemukan')

#cari_data(buka_data)

#========================================= 
#Praktikun 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 4 : Membuat fungsi update nilai
#========================================= 

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru >100 :
        print("NIlai harus antara 0 sampai 100. Update dibatalkan")
    
    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)

#========================================= 
#Praktikun 2 : Konsep ADT dan File Handling (studi kasus)
#Latihan Dasar 5 : Membuat fungsi menyimpan data  ke dalam file
#=========================================

def simpan_data(nama_file,data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted (data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file,buka_data)
#print("Data berhasil disimpan")

#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan Dasar 6: Membuat Menu
#====================================================

def main():
   

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. keluar")

        pilihan = input("Pilihan menu: ").strip()
        if pilihan=="1":
            tampilkan_data(buka_data)

        elif pilihan=="2":
            cari_data(buka_data)

        elif pilihan=="3":
            update_nilai(buka_data)

        elif pilihan=="4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()