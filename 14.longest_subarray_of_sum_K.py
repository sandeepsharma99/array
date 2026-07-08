# <--------------Brute force--------------------->

# def longest_subarray(array,t):
#     n = len(array)

#     for i in range(n):
#         for j in range(n):
#             summ = 0
#             size = 0
#             for k in range(0,j-i+1):
#                 summ+=array[k]
#             if summ == t:
#                 size = max(size,k-i+1)

#     return len(size)

# <----------------Hasing----------------------->

# TC O(n logn ) if sorted else O(n^2) SC O(n)

# def longest_subarray_with_sum_k(nums, k):
#     # Dictionary to store:
#     # prefix_sum -> first index where this prefix sum occurred
#     prefix_sum_map = {}

#     # Running sum of elements
#     prefix_sum = 0

#     # Stores the maximum length of a subarray with sum = k
#     max_len = 0

#     # Traverse the array
#     for i in range(len(nums)):

#         # Add current element to the running sum
#         prefix_sum += nums[i]

#         # Case 1:
#         # If the prefix sum itself equals k,
#         # then the subarray from index 0 to i has sum = k
#         if prefix_sum == k:
#             max_len = max(max_len, i + 1)

#         # We need to check whether there exists a previous prefix sum
#         # equal to (current_prefix_sum - k)
#         rem = prefix_sum - k

#         # If such a prefix sum exists,
#         # then the subarray between those two indices has sum = k
#         if rem in prefix_sum_map:
#             length = i - prefix_sum_map[rem]
#             max_len = max(max_len, length)

#         # Store only the FIRST occurrence of every prefix sum.
#         # This helps us get the longest possible subarray.
#         if prefix_sum not in prefix_sum_map:
#             prefix_sum_map[prefix_sum] = i

#     return max_len

#<--------------------Two pinter------------------------------->
# def longest_subarray_with_sum_k(nums, k) :
#     summ = 0
#     i = j = 0
#     max_len = 0

#     # st = -1
#     # ed = -1

#     n = len(nums)
#     while j < n :
#         summ+=nums[j]
#         # shrink if sum got greator
#         while i <= j and summ > k :
#             summ-=nums[i]
#             i+=1
#         # summ equal to K
#         if summ==k :
#             max_len = max(max_len,j-i+1)

#             # st = i
#             # ed = j
#         while i <= j and summ > k :
#             summ-=nums[i]
#             i+=1

#         j+=1
#     # if st == -1:
#     #     return []
#     return max_len 
# # Example
# nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
# k = 6

# print(longest_subarray_with_sum_k(nums, k))


def longest_subarray_with_sum_k(nums, k):
    summ = 0
    i = j = 0
    max_len = 0

    st = -1
    ed = -1

    n = len(nums)

    while j < n:
        summ += nums[j]

        # Shrink window if sum becomes greater than k
        while i <= j and summ > k:
            summ -= nums[i]
            i += 1

        # Found a valid subarray
        if summ == k:
            if j - i + 1 > max_len:
                max_len = j - i + 1
                st = i
                ed = j

        j += 1

    if st == -1:
        return []

    return max_len, nums[st:ed+1]


# Example
nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 6

print(longest_subarray_with_sum_k(nums, k))