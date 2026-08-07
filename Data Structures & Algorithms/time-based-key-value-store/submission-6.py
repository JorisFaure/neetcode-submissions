from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timemap[key]) == 0 :
            return ""
        if timestamp < self.timemap[key][0][1] :
            #on recherche quelque chose d'inferieur au minimum de nos timestamp
            return ""

        left = 0
        right = len(self.timemap[key]) - 1
        print("Salut")
        mid = 0
        while left <= right :
            mid = (left+right)//2
            print(mid)
            if timestamp == self.timemap[key][mid][1] :
                return self.timemap[key][mid][0]
            elif timestamp > self.timemap[key][mid][1] :
                left = mid+1
            else :
                right = mid-1
        return self.timemap[key][(left+right)//2][0]
        
