'''
TC O(n logn) n , SC :O(N)
'''
def merge(intervals):
        intervals.sort(key = lambda ghanta: ghanta[0])
        merge = []

        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else :
                merge[-1] = [min(merge[-1][0],interval[0]), max(merge[-1][1],interval[1])]
                
        return merge

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))