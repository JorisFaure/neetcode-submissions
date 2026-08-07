class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals :
            return []
        res = []
        n = 0
        intervals.sort(key = lambda x : x[0])
        res.append(intervals[0])

        i = 1

        while i < len(intervals):
            #si overlap, alors on append pas
            if res[-1][1] > intervals[i][0] :
                if res[-1][1] > intervals[i][1] :
                    res[-1] = intervals[i]
                i+=1
                n+=1
                continue
            else :
                res.append(intervals[i])
            i+=1
        return n
                
                
