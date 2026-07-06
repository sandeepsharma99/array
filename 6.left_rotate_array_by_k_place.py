# <-----------Brute force-------------->

# def rotate_array_by_k(array,k):
#     n = len(array)
#     d = k%n

#     # temp = [array[i] for i in range(d,n)]
#     temp = array[:d]

#     for i in range(n-d):
#         array[i] = array[i+d]
    
#     for i in range(d):
#         array[n-d+i] = temp[i]
    
#     return array


# <-----------optimize code-------------->

def rotate_array_by_k(array,k):
    n = len(array)
    d = k%n

    array[:d].reverse()

    array[d:].reverse()

    array.reverse()
    return array

array = [1,2,3,4,5,6,7,8,9]
k = 12

print(rotate_array_by_k(array, k))