'''
    Brute force
'''

def foursum(nums, target) :
    n = len(nums)
    st = set()

    for i in range(n) :
        for j in range(i+1,n) :
            for k in range(j+1, n) :
                for l in range(k+1,n) :
                    total = nums[i] + nums[j] +nums[k] + nums[l]
                    if total == target :
                        temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                        st.add(tuple(temp))