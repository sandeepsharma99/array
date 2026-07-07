def intersection(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    intersec = []
    
    while i<n and j<m :
        if arr1[i]<arr2[j] :
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else :
            intersec.append(arr1[i])
            i+=1
            j+=1

    return intersec


arr1 = [1,3,5,9,10]
arr2 = [0,2,3,5,4,7,9,6,3,2]

print(intersection(arr1, arr2))