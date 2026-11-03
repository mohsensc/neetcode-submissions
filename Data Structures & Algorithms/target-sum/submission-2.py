class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def tracker(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if  (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = (tracker(i+1, total - nums[i]) +
            tracker(i+1, total + nums[i]))

            return cache[(i, total)]
        
        return tracker(0,0)