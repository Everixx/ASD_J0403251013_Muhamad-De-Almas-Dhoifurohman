#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Materi rekursif : Faktorial
# recursive case=> 3! = 3 x 2 x 1
# base case => 0 berhenti
#=======================================================================================

def faktorial(n):
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1) #n-1*n-2*n-3.....n*?
print("==== Program Faktorial ====")
a=int(input("Masukan bilangan faktorial : "))
print("Hasil faktorial : ", faktorial(a))


