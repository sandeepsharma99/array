def majority(array) :
    count1 = count2 = 0
    ele1 = ele2 = 0 
    n = len(array)
    for i in range(n):
        if count1 == 0 and array[i]!= ele2:
            ele1 = array[i]  
            count1 =1
        elif count2 == 0 and array[i]!= ele1:
            ele2 = array[i]
            count2 =1
        elif array[i] == ele1 :count1 +=1
        elif array[i] == ele2 :count2 +=1
        else :
            count1 -=1
            count2 -=1

    # Important: Their counts (count1 and count2) are not their actual frequencies.
    count1 = count2 = 0 # reset count 
    for num in array :
        if num == ele1 : count1 +=1
        elif num == ele2 : count2 += 1
    voting_count = []
    if count1 > n//3 :
        voting_count.append(ele1)
    if count2 > n//3 : 
        voting_count.append(ele2)

    return voting_count


array = [3,2,3,2,1,0,3]
print(majority(array))