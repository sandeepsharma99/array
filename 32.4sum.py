'''
    Brute force 
    O(n⁴ × log M)
'''

# def foursum(nums, target) :
#     n = len(nums)
#     st = set()

#     for i in range(n) :
#         for j in range(i+1,n) :
#             for k in range(j+1, n) :
#                 for l in range(k+1,n) :
#                     total = nums[i] + nums[j] +nums[k] + nums[l]
#                     if total == target :
#                         temp = sorted([nums[i], nums[j], nums[k], nums[l]])
#                         st.add(tuple(temp))
    
#     ans = [list(quad) for quad in st] # [-2, -1, 1, 2] , [-1, 0, 0, 1] , [-2, 0, 0, 2] 
#     return ans

# nums = [1,0,-1,0,-2,2] 
# target = 0

# print(foursum(nums, target))

'''
POINTER APPROACH  TC : O(n³)  SC O(1)
'''

def four_sum(nums, target):
    n = len(nums)
    ans = []

    nums.sort()

    for i in range(n):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # Skip duplicate values for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])

                    k += 1
                    l -= 1

                    # Skip duplicate values for k
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                    # Skip duplicate values for l
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1
                else:
                    l -= 1

    return ans


# Example
nums = [1, 0, -1, 0, -2, 2]
target = 0

print(four_sum(nums, target))