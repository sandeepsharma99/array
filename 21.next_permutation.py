def nextPermutation( nums) :
        ind = -1
        n = len(nums)

        # Step 1: Find the pivot
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # Step 2: If no pivot exists, reverse the entire array
        if ind == -1:
            nums.reverse()
            return nums

        # Step 3: Find the next greater element from the right
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 4: Reverse the suffix
        left = ind + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
        
nums = [1,2,3]
print(nextPermutation(nums))