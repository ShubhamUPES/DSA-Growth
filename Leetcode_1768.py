class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = list(word1)
        b = list(word2)
        result = ""

        min_len = min(len(a), len(b))
        for i in range(min_len):
            result += a[i] + b[i]
        result += ''.join(a[min_len:]) + ''.join(b[min_len:])

        return result
