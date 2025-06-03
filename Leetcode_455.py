from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes
        g.sort()
        s.sort()

        # Initialize two pointers: one for children (i), one for cookies (j)
        i = j = 0

        # Iterate until we either run out of children or cookies
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # If the current cookie satisfies the child, move to next child
                i += 1
            # Move to next cookie regardless of whether the current one was used
            j += 1
        
        # i will represent the number of content children
        return i
