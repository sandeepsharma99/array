def longest_successive_elements(array):
    n = len(array)
    if n == 0:
        return 0

    longest = 1

    # Create a set containing all elements
    st = set(array)

    # Iterate through each element in the set
    for num in st:

        # Check if num is the start of a sequence
        if num - 1 not in st: # previous is not in set
            cnt = 1
            last_smaller = num

            # Count consecutive numbers
            while last_smaller + 1 in st: 
                last_smaller = last_smaller + 1
                cnt += 1

            longest = max(longest, cnt)

    return longest


array = [100, 4, 101, 102, 1, 3, 2]
print(longest_successive_elements(array))