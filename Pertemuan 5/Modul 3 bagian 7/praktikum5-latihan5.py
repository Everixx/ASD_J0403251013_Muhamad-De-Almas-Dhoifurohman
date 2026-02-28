#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

#========================================================== 
# Studi Kasus: Generator PIN
#========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    # Jika panjang PIN sudah sesuai, tampilkan
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
 
    # Tambahkan digit 0, 1, atau 2
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
 
buat_pin(3)

#===============================================================================================
#  Penjelasan
#===============================================================================================
# Fungsi menghasilkan semua kombinasi PIN dengan panjang tertentu menggunakan digit 0, 1, dan 2.
#===============================================================================================
# Contoh untuk panjang = 3:
'''
buat_pin(3)
-> 000
-> 001
-> 002
-> ...
-> 222
'''
# Total kombinasi = 3^n karena setiap posisi memiliki 3 pilihan angka.
'''
Jika ingin mencegah angka yang sama berulang,
tambahkan pengecekan sebelum rekursi agar digit baru
tidak sama dengan digit terakhir pada variabel hasil.
'''