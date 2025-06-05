
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []

        for word in words:
            rows = [0, 0, 0]
            for ch in word.lower():
                if ch in row1:
                    rows[0] = 1
                elif ch in row2:
                    rows[1] = 1
                elif ch in row3:
                    rows[2] = 1

            if sum(rows) == 1:
                result.append(word)

        return result
