#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file
#=========================================

#Membuka file dengan mode read "r"
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("=== Hasil Read ===")
print("Tipe Data:", type(isi_file))    
print("Jumlah Karakter", len(isi_file))
print("Jumlah baris", isi_file.count('\n')+1)

#Membuka file per baris 
print("=== Membaca File per Baris ===")
jumlah_baris=0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris +1
        baris = baris.strip() #strip untuk mengambil datanya saja(menghilangkan garis baru"\n")
        print("Baris ke-", jumlah_baris)
        print("Isinya :", baris)

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Presing baris menjadi kolom data
#=========================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("\nNIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan file
#=========================================
data_list = []
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        #simpan sebagai list " [nim, nama, nilai]"
        nim, nama, nilai = baris.split(",")
        data_list.append([nim,nama,int(nilai)])

print("\n=== Data Mahasiswa dalam LIST ===")
print(data_list)

print("\n=== Jumlah Record Dalam LIST ===")
print("Jumlah Record", len(data_list))

print("\n=== Menampilkan Data Record Terterntu ===")
print("Contoh Record Pertama:", data_list[0])

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary
#=========================================

data_dict = {} #buat variabel untuk dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim]= {            #key
            "nama": nama,            #value
            "nilai": int(nilai)      #values
        }
print("\n=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)