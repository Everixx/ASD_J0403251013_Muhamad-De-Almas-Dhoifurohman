#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

#========================================================== 
# Latihan 2: Proses Rekursi Perpangkatan
#==========================================================

def pangkat(a, n):
    # Kondisi berhenti
    if n == 0:
        return 1

    # Proses rekursif
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))

#===============================================================================
# Penjelasan
#===============================================================================
# Fungsi menghitung a^n dengan mengalikan a secara berulang sampai n bernilai 0.
#===============================================================================
# Urutan pemanggilan:
'''
pangkat(2,4)
-> 2 * pangkat(2,3)
-> 2 * pangkat(2,2)
-> 2 * pangkat(2,1)
-> 2 * pangkat(2,0) = 1
'''