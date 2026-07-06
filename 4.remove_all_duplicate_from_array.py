def remove_duplicate(array):
    array.sort()
    i = 0
    for j in range(1,len(array)):
        if array[j] != array[i]:  # if it is different
            array[i+1] = array[j] # move curr ele to i+1 
            i+=1  
    return array[ :i+1]

array = [1,1,3,3,2,3,2,4,4,4,4]

print(remove_duplicate(array))