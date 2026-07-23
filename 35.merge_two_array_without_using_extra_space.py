def merge(arr1, arr2, n, m):
    arr3 = []
    left = 0
    right = 0

    # Merge both arrays
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3.append(arr1[left])
            left += 1
        else:
            arr3.append(arr2[right])
            right += 1

    # Copy remaining elements of arr1
    while left < n:
        arr3.append(arr1[left])
        left += 1

    # Copy remaining elements of arr2
    while right < m:
        arr3.append(arr2[right])
        right += 1

    # Copy back to arr1 and arr2
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]


# Example
arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

merge(arr1, arr2, len(arr1), len(arr2))

print(arr1)
print(arr2)