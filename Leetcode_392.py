
correct:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)









'''class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        a = list(t)
        b = list(s)
        for i in range(len(b)):
            for j in range(len(a)):
                if b[i] == a[j]:
                    count += 1
                    break  # stop inner loop after first match for this char
        return count == len(s)'''
