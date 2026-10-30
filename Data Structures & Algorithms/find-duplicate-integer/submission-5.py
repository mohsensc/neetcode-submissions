class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = start = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while True:
            start = nums[start]
            slow = nums[slow]
            if slow == start:
                return start

        
