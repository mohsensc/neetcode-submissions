class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig = {2: ("a","b","c"), 3: ("d","e","f"), 4: ("g","h","i"), 5: ("j","k","l"), 6: ("m",'n',"o"), 7: ('p','q','r','s'), 8: ('t','u','v'), 9: ('w','x','y','z')}

        l = [int(i) for i in digits]
        l.append(1)
        answer = []

        def maker(prev, curr):
            if curr[0] == 1:
                answer.append(prev)
                return
            
            for i in dig[curr[0]]:
                maker(prev + i, curr[1:])
        
        maker("", l)
        
        return [] if answer == [""] else answer
