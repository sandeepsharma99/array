# < ------------Using hashset------------------ >
'''
TC O (n^2 logn)

'''

def triplet(nums):
    st = set()
    n = len(nums)

    for i in range(n):
        hashset = set()

        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])

            if third in hashset:
                temp = sorted([nums[i], nums[j], third])
                st.add(tuple(temp))   # imp: set stores tuples, not lists

            hashset.add(nums[j])

    ans = [list(triplet) for triplet in st]
    return ans


nums = [-1, 0, 1, 2, -1, -4]
print(triplet(nums))