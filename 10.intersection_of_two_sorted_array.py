

def intersection(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    intersec = []
    
    while i<n and j<m :  # till any array ends
        if arr1[i]<arr2[j] :
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else :
            if not intersec or arr1[i] != intersec[-1]: # is empty and different
                intersec.append(arr1[i])
                i+=1
                j+=1

    return intersec


arr1 = [1,3,5,9,10]
arr2 = [0,2,3,5,4,7,9,6,3,2]

print(intersection(arr1, arr2))

# TC O(n1 + n2)
# SC O(1)