
def max_len(arr):
    mpp = {}
    max_len = 0
    total = 0

    start = -1
    end = -1

    for i in range(len(arr)):
        total += arr[i]

        if total == 0:
            max_len = i + 1 
            start = 0
            end = i

        else:
            if total in mpp:
                length = i-mpp[total]
                max_len = max(max_len, length)
                start = mpp[total]+1
                end = i
            else:
                mpp[total] = i # if not then put

    return max_len , arr[start: end+1]


# Example
arr = [9, -3, 3, -1, 6, -5]
print(max_len(arr))