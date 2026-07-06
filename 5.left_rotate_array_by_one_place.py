
def rotate_by_one(array):
    n = len(array)
    temp = array[0]
    for i in range(1,n):
        array[i-1] = array[i]
        
    array[n-1] = temp

    return array

array = [1,2,3,4,5,6]

print(rotate_by_one(array))