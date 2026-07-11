# boyer's Moore voting algorith
def majority_element(array) :
    n = len(array)//2
    count = 0
    ele = -1
    for num in array :
        if count == 0 :
            ele = num
            count = 1
        elif ele == num :
            count += 1
        else :
            count -= 1
        
    # return ele

        if array.count(ele) > n/2:
            return ele
        else :
            -1


array = [2,2,1,1,1,1,1,1,2,2]
print(majority_element(array))
        

