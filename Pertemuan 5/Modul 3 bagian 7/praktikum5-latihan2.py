#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

#========================================================== 
# Latihan 2: Tracing Rekursi
#==========================================================

def countdown(n):
    # Kondisi berhenti
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)     # Sebelum rekursi
    countdown(n - 1)       # Pemanggilan rekursif
    print("Keluar:", n)    # Setelah rekursi

countdown(3)

#===============================================================================
# Penjelasan
#===============================================================================
''' 
Baris ‘Keluar’ dicetak terakhir karena rekursi harus menyelesaikan 
pemanggilan fungsi terdalam terlebih dahulu sebelum kembali ke baris setelahnya.
'''
#===============================================================================
# Fungsi menampilkan urutan masuk dan keluar pada proses rekursi.
#===============================================================================
# Urutan pemanggilan:
'''
countdown(3)
-> Masuk 3
-> Masuk 2
-> Masuk 1
-> Selesai
-> Keluar 1
-> Keluar 2
-> Keluar 3
'''