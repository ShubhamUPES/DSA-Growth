from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_p = len(p)
        len_s = len(s)
        
        if len_s < len_p:
            return result
        
        p_count = Counter(p)
        window_count = Counter(s[:len_p])
        
        if window_count == p_count:
            result.append(0)
        
        for i in range(len_p, len_s):
            start_char = s[i - len_p]
            end_char = s[i]
            
            window_count[end_char] += 1
            window_count[start_char] -= 1
            
            # Remove character count if it drops to 0
            if window_count[start_char] == 0:
                del window_count[start_char]
            
            if window_count == p_count:
                result.append(i - len_p + 1)
        
        return result
