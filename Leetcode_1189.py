correct:

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )

'''my approach correct too:
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = list(text)
        d = list("balloon")
        count = 0
        
        while True:
            temp_b = b[:]
            can_form = True
            
            for char in d:
                if char in temp_b:
                    temp_b.remove(char)
                else:
                    can_form = False
                    break
            
            if can_form:
                count += 1
                b = temp_b
            else:
                break
        
        return count
'''
