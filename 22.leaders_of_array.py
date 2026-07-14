def leaders(array) :
    n = len(array)
    maxi = float("-inf")
    ans = []
    for i in range(n-1,-1,-1) :
        if array[i] > maxi :
            ans.append(array[i])
        maxi = max(maxi, array[i])
    
    ans.sort()
    return ans
    
    

array = [16, 17, 4, 3, 5, 2]
print(leaders(array))
