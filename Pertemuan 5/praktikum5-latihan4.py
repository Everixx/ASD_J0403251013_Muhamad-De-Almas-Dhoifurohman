#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

#========================================================== 
# Latihan 4: Kombinasi Huruf
#========================================================== 
 
def kombinasi(n, hasil=""): 
 
    # Jika panjang sudah n, tampilkan hasil
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # Tambah huruf A
    kombinasi(n, hasil + "A") 
    
    # Tambah huruf B
    kombinasi(n, hasil + "B") 
 
 
kombinasi(2)


#===============================================================================
# Penjelasan
#===============================================================================
# Fungsi membentuk semua kemungkinan susunan huruf A dan B
# dengan panjang sesuai nilai n.
#===============================================================================
# Urutan untuk n = 2:
'''
kombinasi(2)
-> AA
-> AB
-> BA
-> BB
'''
# Total kombinasi = 2^n karena setiap posisi memiliki 2 pilihan (A atau B).