"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for i in range(len(intervals)) :
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()
        

        
        
        
        i = 0
        j = 0

        max_meeting_point = 0
        curr_meeting_point = 0

        while i < len(start) :
            if start[i] < end[j] :
                curr_meeting_point += 1
                max_meeting_point = max(max_meeting_point, curr_meeting_point)
                i+=1
            else :
                curr_meeting_point -=1
                j+=1
        return max_meeting_point


            
            

        