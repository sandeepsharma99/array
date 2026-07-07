def intersection(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    intersec = []
    
    for num in arr1:
        if num in arr2:
            intersec.append(num)
            i +=1


    return intersec 


arr1 = [1,3,5,9,10]
arr2 = [0,2,3,5,4,7,9,6,3,2]

print(intersection(arr1, arr2))