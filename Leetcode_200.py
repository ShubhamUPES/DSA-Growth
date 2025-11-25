class Solution:
    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0                     # → Important: handle empty grid

        count = 0                        # → Number of islands
        n = len(grid)                    # → rows
        m = len(grid[0])                 # → cols

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
                return                   # → Out of bounds / water / visited

            grid[i][j] = '0'             # → Mark visited (sink land)

            dfs(i + 1, j)                # down
            dfs(i - 1, j)                # up
            dfs(i, j + 1)                # right
            dfs(i, j - 1)                # left

        for i in range(n):               # → O(n × m)
            for j in range(m):
                if grid[i][j] == '1':    # → Found new island
                    dfs(i, j)            # → Flood fill
                    count += 1

        return count                     # → Total islands
