class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):  # loop until the last possible start index
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i  # matched all characters
        return -1
