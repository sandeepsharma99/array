def longest_successive_element(array) :
    n = len(array)
    if n ==0 :
        return 0
    # Create a set containing all elements
    st = set (array)
    longest = 0
    count = 0

    # Iterate through each element in the set
    for num in array :
        # Check if num is the start of a sequence
        if num -1 not in st : # check if previous is not present
            count = 1
            next_conseutive = num+1 # what is consecutive
            
            # Count consecutive numbers
            while next_conseutive in st :
                next_conseutive = next_conseutive +1
                count +=1 
            longest = max(longest, count)
            

    return longest

array = [100, 4, 200, 1, 3, 2]
print(longest_successive_element(array))

