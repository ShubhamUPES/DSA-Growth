class Solution:
    def areAnagrams(self, s1, s2):
        return sorted(s1) == sorted(s2)
