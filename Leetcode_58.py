class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.split()
        return len(d[-1])
