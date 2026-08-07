class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        for c in s1 :
            hashmap_s1[c] = hashmap_s1.get(c, 0) + 1
        begin = 0
        hashmap_s2 = {}
        count_s2 = 0
        for end in range(len(s2)) :
            hashmap_s2[s2[end]] = hashmap_s2.get(s2[end], 0) + 1
            count_s2 += 1
            if count_s2 > len(s1) :
                hashmap_s2[s2[begin]] -=1
                if hashmap_s2[s2[begin]] == 0 :
                    hashmap_s2.pop(s2[begin], None)
                begin += 1
                count_s2 -= 1
            print(hashmap_s2, hashmap_s1)
            if hashmap_s2 == hashmap_s1 :
                return True
        return False
            
            





        