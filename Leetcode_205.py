class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        u = list(s)
        v = list(t)

        pattern_s = []
        pattern_t = []

        for i in range(len(u)):
            pattern_s.append(u.index(u[i]))
            pattern_t.append(v.index(v[i]))

        return pattern_s == pattern_t
