class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges)+1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return [a, b]
            parent[pb] = pa
        
        return []
        