"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals :
            return 0
        res = 1
        start = []
        intervals.sort(key = lambda x : x.start)
        for i in range(0, len(intervals)) :
            start.append(intervals[i].start)

        
        end = []
        intervals.sort(key = lambda x : x.end)
        for i in range(0, len(intervals)) :
            end.append(intervals[i].end)
        
        s = 0
        e = 0
        max_c = 0
        count = 0

        while s < len(start) :
            if start[s] < end[e] :
                count+=1
                s+=1
            else :
                count-=1
                e+=1

            max_c = max(max_c, count)

        return max_c
            


        