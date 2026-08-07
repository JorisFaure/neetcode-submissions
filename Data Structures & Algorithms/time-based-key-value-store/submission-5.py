from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        timestamp_list = list(self.timemap[key].keys())
        if len(timestamp_list) == 0 :
            return ""
        if timestamp < timestamp_list[0] :
            #on recherche quelque chose d'inferieur au minimum de nos timestamp
            return ""

        left = 0
        l = len(timestamp_list) - 1
        right = l
        print("Salut")
        mid = 0
        while left <= right :
            mid = (left+right)//2
            print(mid)
            if timestamp == timestamp_list[mid] :
                return self.timemap[key][timestamp]
            elif timestamp > timestamp_list[mid] :
                left = mid+1
            else :
                right = mid-1
        prev_timestamp = timestamp_list[(left+right)//2]
        return self.timemap[key][prev_timestamp]
        
