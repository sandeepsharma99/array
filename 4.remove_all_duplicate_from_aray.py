def remove_duplicate(array):
    i = 0
    for j in range(1,len(array)):
        if array[j] != array[i]:
            array[i+1] = array[j]
            i+=1
    return array[ :i+1]
array = [1,1,2,2,2,3,3,3,4,4,4,4]

print(remove_duplicate(array))