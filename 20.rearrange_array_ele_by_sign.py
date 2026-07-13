def rearrange(array) :
            pos = []
            neg = []
            for i in range(len(array)) :
                if array[i] > 0 :
                    pos.append(array[i])
                else :
                    neg.append(array[i])
            
            if len(pos) > len(neg) : # case 1: if pos ele > neg ele
                for i in range(len(neg)) :
                    array[2*i] = pos[i]
                    array[2*i+1] = neg[i]
                
                j = len(neg)*2
                for i in range(len(neg),len(pos)) : #
                    array[j] = pos[i] # i = 3,4, j = 6,7
                    j+=1
            else :                          # case 2: if neg ele > pos ele
                for i in range(len(pos)) :
                    array[2*i] = pos[i]
                    array[2*i+1] = neg[i]
                
                j = len(pos)*2
                for i in range(len(pos),len(neg)) :
                    array[j] = neg[i]   
                    j+=1

            return array

array = [3,1,-2,-5,2,-4,2,4]

print(rearrange(array))

# TC O(n) sc  O(n)