

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [""] * n
        score_with_index = []
        for i in range(n):
            score_with_index.append((score[i], i))

        score_with_index.sort(reverse=True)

        for rank in range(n):
            value, index = score_with_index[rank]
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result
