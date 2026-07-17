def find_all_subarrays_with_given_sum(arr, k):
    mpp = {}
    mpp[0] = 1

    pre_sum = 0
    count = 0

    for num in arr:
        pre_sum += num
        remove = pre_sum - k

        count += mpp.get(remove, 0)
        mpp[pre_sum] = mpp.get(pre_sum, 0) + 1

    return count

array = [1,2,3]
k = 3
print(find_all_subarrays_with_given_sum(array,k))