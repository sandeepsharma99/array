# # kadane's algorith
# # TC O(n) sc o(1)

# def maximum_subarray_sum(array) :
#     max_sum = float("-inf") 
#     summ = 0

#     for i in range(len(array)) :
#         summ += array[i]
#         if summ < 0:
#             summ = 0
#         max_sum = max(max_sum,summ)

#     return max_sum
    

# array = [-2,1,-3,4,-1,2,1,-5,4]

# print(maximum_subarray_sum(array))


# kadane's algorith
# TC O(n) sc o(1)

def maximum_subarray_sum(array) :
    max_sum = float("-inf") 
    summ = 0
    start = 0
    ans_start = 0
    ans_end = 0

    for i in range(len(array)) :
        # if stating a new subarray :
        if summ == 0 :
            start = i

        summ += array[i]

        if summ < 0:
            summ = 0
        
        if summ >max_sum :
            max_sum = max(max_sum,summ)
            ans_start = start
            ans_end = i
        

    return max_sum , array[ans_start : ans_end+1]
    

array = [-2,1,-3,4,-1,2,1,-5,4]

print(maximum_subarray_sum(array))