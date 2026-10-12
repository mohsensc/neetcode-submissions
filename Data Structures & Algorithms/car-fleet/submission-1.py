from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = deque()
        pairs = [[position[i],speed[i]]for i in range(len(position))]

        pairs.sort(key = lambda x: x[0])
        
        for p, s in pairs[::-1]:

            arrivalTime = (target - p) / s
            stack.append(arrivalTime)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
