def largest( array):
    n = len(array)
    largest = 1 # any random smaller value  
    for i in range(n): # loop n times
        if array[i] > largest:
            largest = array[i]
    
    return largest


array = [1,2,3,4,5,6,7]
print(largest(array))