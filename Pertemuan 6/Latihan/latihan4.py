#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

# ==========================================================
# Praktikum 6 - Latihan 4
# Memahami Kode Program (Merge Sort) 
# ==========================================================

def merge_sort(data): 
    if len(data) <= 1: 
        return data 
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right) 
     
    return merge(left_sorted, right_sorted) 

#=============================================================
# Latihan
#=============================================================
'''
Soal
1. Apa yang dimaksud dengan base case? 
2. Mengapa fungsi memanggil dirinya sendiri? 
3. Apa tujuan fungsi merge()? 
'''
#=============================================================
'''
Jawaban
1. Base case adalah kondisi yang menghentikan proses rekursi.  
   Pada kode di atas, base case terjadi ketika panjang data kurang dari atau sama dengan 1, 
   karena data tersebut sudah dianggap terurut.
2. Fungsi memanggil dirinya sendiri karena merge sort menerapkan konsep rekursi untuk
   membagi data menjadi bagian-bagian yang lebih kecil sampai mencapai base case.
3. Fungsi merge() bertujuan untuk menggabungkan dua list yang sudah terurut menjadi 
   satu list baru yang terurut secara keseluruhan.
'''
