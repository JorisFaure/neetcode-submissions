class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0]*(len(edges)+1)

        def find(x) :
            if x != parent[x] :
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y) :
            root_x = find(x)
            print("hye")
            root_y = find(y)
            print(x,y)

            if root_x == root_y :
                return False

            if rank[root_x] < rank[root_y] :
                parent[root_x] = root_y
            elif rank[root_y] < rank[root_x] :
                parent[root_y] = root_x
            else :
                parent[root_y] = root_x
                rank[root_x]+=1
            return True
        for x,y in edges :
            if not union(x,y) :
                return [x,y]
        return [-1,-1]


        