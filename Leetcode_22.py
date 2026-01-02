class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def backtrack(path, open_cnt, close_cnt):
            if len(path) == 2 * n:
                res.append(path)
                return

            if open_cnt < n:
                backtrack(path + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(path + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res
