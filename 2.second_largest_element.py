def sec_largest(array):
    sorted(array, reverse=True)   # [8, 7, 7, 6, 5, 4, 2, 1]
    largest = float("-inf") # negative infinity
    sec_largest = float("-inf")
    n = len(array)

    # if len(array) < 2:
    #     return -1
    if not array:
        return -1
    else :
        for num in array:
            if num>largest:
                sec_largest = largest
                largest = num
            
            elif num>sec_largest and num<largest:
                sec_largest = num

        return sec_largest, largest


array = [1,2,4,7,7,5,8,6]

print(sec_largest(array))