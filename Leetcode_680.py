class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                a = s[i+1:n - i]      
                b = s[i:n - 1 - i]   
                return a == a[::-1] or b == b[::-1]
        print(True)
        return True
