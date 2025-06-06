

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            temp = list(details[i])
            age = int(temp[11] + temp[12])
            if age > 60:
                count += 1
        return count
