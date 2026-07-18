# def find_all_subarrays_with_given_sum(arr, k):
#     mpp = {}
#     mpp[0] = 1

#     pre_sum = 0
#     count = 0

#     for num in arr:
#         pre_sum += num
#         x = pre_sum - k

#         count += mpp.get(x, 0)
#         mpp[pre_sum] = mpp.get(pre_sum, 0) + 1

#     return count

# array = [1,2,3,-3,1,1,1,4,2,-3]
# k = 3
# print(find_all_subarrays_with_given_sum(array,k))


# < ------------ Extra ----------------------- >

def find_all_subarrays_with_given_sum(arr, k):
    # Dictionary to store prefix sum and the list of indices
    # Prefix sum 0 is considered to occur before the array starts (-1)
    mpp = {0: [-1]}

    pre_sum = 0
    count = 0
    result = []  # Stores all subarrays whose sum is k

    # Traverse the array
    for i, num in enumerate(arr):

        # Update prefix sum
        pre_sum += num

        # Find the required previous prefix sum
        x = pre_sum - k

        # If found, all stored indices form valid subarrays
        if x in mpp:
            for start in mpp[x]:
                # Extract the subarray
                result.append(arr[start + 1:i + 1]) #appends the slice of array
                count += 1

        # Store the current index for this prefix sum
        if pre_sum not in mpp:
            mpp[pre_sum] = []

        mpp[pre_sum].append(i)

    return count, result


array = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3

count, subarrays = find_all_subarrays_with_given_sum(array, k)

print("Count:", count)
print("Subarrays:")
for sub in subarrays:
    print(sub)