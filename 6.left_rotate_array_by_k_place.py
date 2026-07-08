# <-----------Brute force-------------->

def rotate_array_by_k(array,k):
    n = len(array)
    d = k%n

    # temp = [array[i] for i in range(d,n)]
    temp = array[:d] # [1,2,3]

    # putting sec part to front 
    for i in range(n-d):
        array[i] = array[i+d] 
        
    # putting front part to sec
    for i in range(d):
        array[n-d+i] = temp[i]
    
    return array

array = [1,2,3,4,5,6,7,8,9]
k = 12


# <-----------optimize code-------------->

# def rotate_array_by_k(array,k):
#     n = len(array)
#     d = k%n

#     array[:d].reverse() # [3, 2, 1] creates a copy of reverse

#     array[d:].reverse() # [4, 5, 6, 7, 8, 9]

#     array.reverse() # [9,8,7,6,5,4,3,2,1]
#     return array

array = [1,2,3,4,5,6,7,8,9]
k = 12

print(rotate_array_by_k(array, k))