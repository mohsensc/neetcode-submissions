from collections import defaultdict as dd

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        results = [math.inf] * n
        results[src] = 0

        for j in range(k+1):
            prices = results.copy()
            for source, node, price in flights:
                if prices[node] > results[source] + price:
                    prices[node] = results[source] + price
            
            results = prices

        return results[dst] if results[dst] != math.inf else -1

