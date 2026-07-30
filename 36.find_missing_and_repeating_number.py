def find_missing_repeating_numbers(arr):
    n = len(arr)

    # Sum of first n natural numbers
    SN = (n * (n + 1)) // 2

    # Sum of squares of first n natural numbers
    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    S = 0
    S2 = 0

    # Calculate actual sum and sum of squares
    for num in arr:
        S += num
        S2 += num * num

    # x - y
    val1 = S - SN

    # x² - y²
    val2 = S2 - S2N

    # x + y
    val2 = val2 // val1

    # Repeating number (x)
    x = (val1 + val2) // 2

    # Missing number (y) 
    y = x - val1

    return [x, y]

arr = [4,3,6,2,1,1]
print(find_missing_repeating_numbers(arr))



"""gfchjkl;jhgjkltfghjkjlhgfhgjk
ghjkljhgfghjklkjhertyguhijloiuytrrftyuio
ghjghjkg"""