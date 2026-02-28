#==================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#==================================================================

# =================================================================
# Contoh Backtracking 2: Deret Biner dengan Pembatasan Jumlah '1'
# =================================================================
 
def biner_batas(n, batas, hasil="", jumlah_1=0): 
    # Jika total angka '1' sudah melebihi batas, proses dihentikan
    if jumlah_1 > batas: 
        return 
 
    # Kondisi akhir: panjang deret sudah mencapai n
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # Tambahkan karakter '0'
    biner_batas(n, batas, hasil + "0", jumlah_1) 
    
    # Tambahkan karakter '1' dan tingkatkan penghitung jumlah_1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2) 


#=====================================================================================
# KETERANGAN PROSES
#=====================================================================================
# Fungsi ini membentuk semua kemungkinan bilangan biner dengan panjang 4.
# Namun jumlah angka '1' tidak boleh lebih dari 2.
#=====================================================================================
# Mekanisme kerjanya:
'''
1. Setiap langkah memiliki dua pilihan, yaitu menambah '0' atau '1'.
2. Variabel jumlah_1 dipakai untuk mencatat berapa banyak '1' yang sudah digunakan.
3. Jika jumlah_1 melewati batas yang ditentukan, cabang tersebut langsung dihentikan.
'''
#======================================================================================