from collections import Counter 

def singleNumber( nums) :
    count = Counter(nums) # Counter({3: 3, 2: 2, 1: 1})
    for num in count:
        if count[num] == 1:
            return num

nums = [2,2,1]

print(singleNumber(nums))


# TC O(n) SC O(n)