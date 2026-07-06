def linear_search(arary,k):
    for i in range(len(array)):
        if array[i] == k:
            return i
    return -1

array = [1,5,6,2,4,2,5,8,6,2,1,50]
k = 500

print(linear_search(array,k))