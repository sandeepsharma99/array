def move_zero(array):
    n = len(array)
    i = 0
    for j in range(n):
        if array[j]!=0: # if it is different
            array[i], array[j] = array[j], array[i] # swap position
            i+=1

    return array


array = [0,0,2,0,18,0,4,0,5,0,6,0]

print(move_zero(array))