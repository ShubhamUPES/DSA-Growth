
class Solution:
    def findSubString(self, s: str) -> int:
        n = len(s)
        distinct_chars = set(s)
        required = len(distinct_chars)

        freq = {}
        start = 0
        min_len = n
        count = 0

        for end in range(n):
            freq[s[end]] = freq.get(s[end], 0) + 1
            if freq[s[end]] == 1:
                count += 1

            while count == required:
                min_len = min(min_len, end - start + 1)
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    count -= 1
                start += 1

        return min_len
