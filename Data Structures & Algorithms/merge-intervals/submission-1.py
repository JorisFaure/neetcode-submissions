class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1 :
            return intervals
        merged = []
        intervals.sort(key = lambda x: x[0])
        for i in range(1, len(intervals) + 1) :
            current_inter = intervals[i - 1]
            if i == len(intervals) :
                merged.append(current_inter)
                continue
            if current_inter[1] < intervals[i][0] :
                merged.append(current_inter)
            else :
                current_inter[0] = min(current_inter[0], intervals[i][0])
                current_inter[1] = max(current_inter[1], intervals[i][1])
                intervals[i] = current_inter
        return merged
        