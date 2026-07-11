# <*****************Brute Force*******************************>
# TC O(n^2) SC O(n)

# def target_summ_subarray(array,k) : 
#     ans = []
#     for i in range(len(array)) :
#         summ = 0
#         for j in range(i,len(array)) :
#             summ += array[j]
#             if summ == k :
#                 ans.append(array[i:j+1])
#                 break
#             elif  summ > k:
#                 break
#     return ans 

# array = [1,2,3,5,6,4,2,1,3] 
# k = 6

# print(target_summ_subarray(array,k))

# <-----------------with the help of Hashmap--------------------------------->

# TC O(n) SC O(n)
def target_summ_subarray(array, k):
    hash_map = {}
    ans = []
    for i in range(len(array)):
        n = k - array[i]
        hash_map[array[i]] = i
    # 1. If the required number exists in dictionary
    # 2. Make sure it's not the same index
        if n in hash_map and hash_map[n] != i:
            ans.append([array[hash_map[n]], array[i]]) # appending the value usin index

    return ans

array = [1,2,3,5,6,4,2,1,3] 
k = 6

print(target_summ_subarray(array,k))

# leetcode 1.
# class Solution:
#     def twoSum(self, nums, target):
#         hash_map = {}

#         for i in range(len(nums)):
#             num = nums[i]
#             hash_map[num] = i
#             more_needed = target - num

#             if more_needed in hash_map:
#                 return [hash_map[more_needed], i] # returnning the index

        



# nums = [1, 2, 3, 5, 6, 4, 2, 1, 3]
# target = 6

# sol = Solution()
# print(sol.twoSum(nums, target))