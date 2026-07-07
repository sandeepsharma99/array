from collections import Counter 

def singleNumber( nums) :
    count = Counter(nums)
    for num in count:
        if count[num] == 1:
            return num

nums = [2,2,1]

print(singleNumber(nums))


# TC O(n) SC O(n)