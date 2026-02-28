#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

# ==========================================================
# Praktikum 5 - Materi 4
# Backtracking Membentuk Deret Biner
# ==========================================================

def biner(n, hasil=""):
    # Kondisi berhenti: jika panjang karakter sudah sesuai n
    if len(hasil) == n:
        print(hasil)
        return
    
    # Rekursi dengan menambahkan angka 0
    biner(n, hasil + "0")
    
    # Rekursi dengan menambahkan angka 1
    biner(n, hasil + "1")

biner(3)

#=============================================================================================
#Penjelasan Proses:
#Program akan membentuk semua kemungkinan susunan angka biner dengan panjang sesuai nilai n.
#=============================================================================================
''' Cara kerjanya:
#1. Fungsi dipanggil dengan hasil kosong ("").
#2. Setiap langkah akan menambahkan "0" lalu "1".
#3. Jika panjang string sudah mencapai n, maka dicetak.
'''
#==============================================================================================
# Untuk n = 3, urutan yang dihasilkan:
'''
000
001
010
011
100
101
110
111
'''
# Jumlah kombinasi yang terbentuk adalah 2 pangkat n. 
# Karena setiap posisi hanya memiliki dua pilihan yaitu 0 atau 1.
#==============================================================================================
