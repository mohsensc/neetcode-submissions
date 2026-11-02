import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        col = []

        for x, y in points:
            distance = ((x*x + y*y)**2)
            heapq.heappush(col, (distance, [x, y]))
        
        return [heapq.heappop(col)[1] for _ in range(k)]