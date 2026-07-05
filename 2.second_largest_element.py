def sec_largest(array):
    sorted(array, reverse=True)
    # 
    largest = float("-inf")
    sec_largest = float("-inf")
    n = len(array)

    # if len(array) < 2:
    #     return -1
    if not array:
        return -1
    else :
        for i in range(n):
            if array[i]>largest:
                sec_largest = largest
                largest = array[i]
            
            elif array[i]>sec_largest and array[i]<largest:
                sec_largest = array[i]

        return sec_largest, largest


# array = [1,2,4,7,7,5,8,6]
array = []

print(sec_largest(array))