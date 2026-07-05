def checkSorted(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True

array = [1,2,3,4,5,6,7]

print(checkSorted(array))