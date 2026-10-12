class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(curr, sublist):
            if not sublist:
                answer.append(curr)
                return
            
            dfs(curr, sublist[1:])
            dfs(curr + [sublist[0]], sublist[1:])
        
        answer, curr = [], []
        dfs(curr, nums)

        return answer