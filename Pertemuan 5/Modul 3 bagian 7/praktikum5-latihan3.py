#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

#========================================================== 
# Latihan 3: Mencari Nilai Maksimum
#========================================================== 
 
def cari_maks(data, index=0): 
 
    # Kondisi berhenti (elemen terakhir)
    if index == len(data) - 1: 
        return data[index] 
 
    # Rekursi ke elemen berikutnya
    maks_sisa = cari_maks(data, index + 1) 
 
    # Bandingkan nilai sekarang dengan hasil rekursi
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))


#====================================================================================================
# Penjelasan
#====================================================================================================
# Fungsi mencari nilai terbesar dalam list dengan membandingkan setiap elemen melalui proses rekursi.
#====================================================================================================
# Urutan proses (angka = [3,7,2,9,5]):
'''
cari_maks([3,7,2,9,5],0)
-> bandingkan 3 dengan hasil dari index 1
-> bandingkan 7 dengan hasil dari index 2
-> bandingkan 2 dengan hasil dari index 3
-> bandingkan 9 dengan hasil dari index 4
-> elemen terakhir = 5
-> hasil akhir = 9
'''