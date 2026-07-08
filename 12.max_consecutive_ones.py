def find_max_consecutive_ones(nums):
    count = 0 # taking two counter
    maxcount = 0
    n = len(nums)
    for num in nums :
        if num == 1 :
            count+=1
            maxcount = max(maxcount,count) 
        else :
            count = 0 # reset

    return maxcount


nums = [1,1,0,1,1,1]
print(find_max_consecutive_ones(nums))