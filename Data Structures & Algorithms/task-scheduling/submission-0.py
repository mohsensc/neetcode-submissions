from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxheap = [-i for i in Counter(tasks).values()]
        heapq.heapify(maxheap)
        queue = deque()
        time = 0

        while maxheap or queue:
            time += 1
            if maxheap:
                numleft = -heapq.heappop(maxheap)
                numleft -= 1
                if numleft != 0:
                    queue.append((time + n, numleft))
            if queue and queue[0][0] == time:
                heapq.heappush(maxheap, -queue.popleft()[1])

        return time

            
        
