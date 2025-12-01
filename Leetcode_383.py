class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Sort both strings (a → z order)
        r = sorted(ransomNote)
        m = sorted(magazine)

        i = j = 0
        
        # Two-pointer scan (check if all characters of r exist in m)
        while i < len(r) and j < len(m):
            if r[i] == m[j]:
                i += 1
                j += 1
            elif r[i] > m[j]:
                j += 1
            else:
                return False  # magazine letter too small → missing
        
        return i == len(r)
