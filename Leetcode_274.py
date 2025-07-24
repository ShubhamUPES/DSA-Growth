class Solution:
    def hIndex(self, citations: List[int]) -> int:
        b = sorted(citations, reverse=True)
        c = []
        for i in range(len(b)):
            if b[i] >= i + 1:
                c.append(i + 1)
        return max(c) if c else 0
