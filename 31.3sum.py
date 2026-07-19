# < ------------Using hashset------------------ >
'''
TC O (n² logn)

'''

# def triplet(nums):
#     st = set()
#     n = len(nums)

#     for i in range(n):
#         hashset = set()

#         for j in range(i + 1, n):
#             third = -(nums[i] + nums[j])

#             if third in hashset:
#                 temp = sorted([nums[i], nums[j], third])
#                 st.add(tuple(temp))   # imp: set stores tuples, not lists

#             hashset.add(nums[j])

#     ans = [list(triplet) for triplet in st]
#     return ans


# nums = [-1, 0, 1, 2, -1, -4]
# print(triplet(nums))

'''
Three pointer approach optimize
TC O(nlogn + n²)

'''


def threeSum(nums):
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n):
            l, r = i+1, n-1

            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l,r = l+1, r-1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif total > 0:
                    r-=1
                else :
                    l+=1
            
        return result

nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
print(threeSum(nums))
                