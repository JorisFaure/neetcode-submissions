class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1 :
            return intervals
        merged = []
        intervals.sort(key = lambda x: x[0])
        for i, inter in enumerate(intervals) :
            if i == 0 :
                merged.append(inter)
            else :
                if merged[-1][1] >= inter[0] :
                    merged[-1][1] = max(merged[-1][1], inter[1])
                else :
                    merged.append(inter)
        return merged
        