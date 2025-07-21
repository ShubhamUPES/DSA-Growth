class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        n = len(s)
        count = 0
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring):
                    count += 1
                    
        return count
