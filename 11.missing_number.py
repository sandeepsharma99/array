def missing_number(nums):
    n = len(nums)

    for i in range(n+1): # traverse to length +1 index
        if i not in nums:
            return i

nums = [3,0,1]

print(missing_number(nums))
