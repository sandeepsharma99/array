# def merge(arr1, arr2, n, m):
#     arr3 = []
#     left = 0
#     right = 0

#     # Merge both arrays
#     while left < n and right < m:
#         if arr1[left] <= arr2[right]:
#             arr3.append(arr1[left])
#             left += 1
#         else:
#             arr3.append(arr2[right])
#             right += 1

#     # Copy remaining elements of arr1
#     while left < n:
#         arr3.append(arr1[left])
#         left += 1

#     # Copy remaining elements of arr2
#     while right < m:
#         arr3.append(arr2[right])
#         right += 1

#     # Copy back to arr1 and arr2
#     for i in range(n + m):
#         if i < n:
#             arr1[i] = arr3[i]
#         else:
#             arr2[i - n] = arr3[i]


# # Example
# arr1 = [1, 4, 8, 10]
# arr2 = [2, 3, 9]

# merge(arr1, arr2, len(arr1), len(arr2))

# print(arr1)
# print(arr2)


class Solution:
    def swap_if_greater(self, arr1, arr2, ind1, ind2):
        if arr1[ind1] > arr2[ind2]:
            arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

    def merge(self, arr1, arr2, n, m):
        length = n + m
        gap = (length // 2) + (length % 2)

        while gap > 0:
            left = 0
            right = left + gap

            while right < length:

                # left in arr1, right in arr2
                if left < n and right >= n:
                    self.swap_if_greater(arr1, arr2, left, right - n)

                # left and right both in arr2
                elif left >= n:
                    self.swap_if_greater(arr2, arr2, left - n, right - n)

                # left and right both in arr1
                else:
                    self.swap_if_greater(arr1, arr1, left, right)

                left += 1
                right += 1

            if gap == 1:
                break

            gap = (gap // 2) + (gap % 2)

