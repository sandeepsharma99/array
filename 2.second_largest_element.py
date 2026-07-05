def sec_largest(array):
    largest = 0
    sec_largest = 0
    n = len(array)
    for i in range(n):
        if array[i]>largest:
            sec_largest = largest
            largest = array[i]
        
        elif array[i]>sec_largest and array[i]<largest:
            sec_largest = array[i]

    return sec_largest, largest


array = [1,2,4,7,7,5,8,6]

print(sec_largest(array))