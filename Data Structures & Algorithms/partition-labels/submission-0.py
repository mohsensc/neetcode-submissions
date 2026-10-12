from collections import defaultdict as dd, deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dic, answer, chars = dd(int), [], set()

        for i in s:
            dic[i] += 1
        
        counter = 0

        for i in s:
            counter += 1
            dic[i] -= 1
            chars.add(i)

            if dic[i] == 0:
                chars.remove(i)
            
            if not chars:
                answer.append(counter)
                counter = 0
        
        return answer

