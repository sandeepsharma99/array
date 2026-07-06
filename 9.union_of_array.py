def union_of_array(arr1, arr2):
    s = set()

    for i in range(len(arr1)):
        s.add(arr1[i])

    for i in range(len(arr2)):
        s.add(arr2[i])
    
    temp = []

    for item in s:
        temp.append(item)

    return temp 

# <----------------Two pointer approach----------------------->

def union_of_array(arr1, arr2):
    i = j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not ans or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1
        else:
            if not ans or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not ans or ans[-1] != arr1[i]:
            ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not ans or ans[-1] != arr2[j]:
            ans.append(arr2[j])
        j += 1

    return ans

arr1 = [1,5,6,7,]
arr2 = [1,2,4,3,6,2,7]

print(union_of_array(arr1,arr2))