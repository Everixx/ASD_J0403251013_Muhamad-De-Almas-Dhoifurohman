#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Materi rekursif : Call Stack 
# Tracing bilangan (masuk - keluar)
# Input 3 
# Masuk 3-2-1 
# Keluar 1-2-3
#=======================================================================================

def hitung(n):

    #base case
    if n ==0:
        print("\nSelesai\n")
        return

    print("Masuk :", n)
    hitung(n-1) #recursive case
    print("Keluar", n)

while True:
    a=int(input("Masukan bilangan tracing :")) 
    print("\n=== Program Tracing ===")
    hitung(a)