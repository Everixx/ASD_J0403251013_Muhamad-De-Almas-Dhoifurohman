#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Merge Sort(Ascending)
#=======================================================================================

def merge_sort(data, depth=0):
    indent = " " * depth #indentasi berdasarkan level rekursif
    print(f"{indent}merge_sort(data)")

    if len(data) <= 1:
        return data
    # Dividide : membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent} divide -> {left} | {right}")

    # recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merger ->{left_sorted} + {right_sorted} = {merged}")

    return merged
def merge(left,right):
    result =[]
    i = 0
    j = 0

    # Membandingkan elemen kiri dan kanan 
    while i < len(left) and j < len(right):
        if left [i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1 #geser index ke kanan
        # menambahkan sisa elemen jika ada

    #menambahkan sisa elemen jika ada
    result.extend(left[i:]) #tambahkan sisa elemen kiri
    result.extend(right[j:]) #tambahkan sisa elemen kanan
    return result

angka = [38, 27, 43, 3, 9, 82, 10]
print("Hasil sorting:" , merge_sort(angka))

