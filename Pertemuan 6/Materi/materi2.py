#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Insertion Sort (Ascending)
#=======================================================================================

def insertion_sort(data):
    #mulai dari awal
    print("Data Awal", data)
    print("="*50)

    # Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen di bagian kiri
        
        print("Iterasi ke-", i)
        print("Nilai key =", key)
        print("Bagian kiri (terurut)", data[:i])
        print("Bagian kanan (belum terurut)", data[i:])
        
        #geser
        while j>=0 and data [j] > key:
            data[j+1]=data[j]
            j-=1
        #sisipkan key ke posisi yang benar
        data[j+1]=key
    return data
angka =[7,8,5,2,4,6]
print("Hasil sorting:",insertion_sort(angka))


