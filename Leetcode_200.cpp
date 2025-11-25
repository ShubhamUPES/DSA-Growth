class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {

        if (grid.empty() || grid[0].empty())
            return 0;                               // → Important: handle empty grid

        int count = 0;                              // → Number of islands
        int n = grid.size();                        // → rows
        int m = grid[0].size();                     // → cols

        for (int i = 0; i < n; i++) {               // → O(n × m)
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {            // → Found land → new island
                    dfs(grid, i, j);                // → Flood fill the island
                    count++;                        // → Increase island count
                }
            }
        }

        return count;                               // → Total islands
    }

private:
    void dfs(vector<vector<char>>& grid, int i, int j) {

        if (i < 0 || i >= grid.size() ||            // → Out of bounds
            j < 0 || j >= grid[0].size() ||
            grid[i][j] == '0')
            return;                                 // → Already water/visited

        grid[i][j] = '0';                           // → Mark visited (sink land)

        dfs(grid, i + 1, j);                        // down
        dfs(grid, i - 1, j);                        // up
        dfs(grid, i, j + 1);                        // right
        dfs(grid, i, j - 1);                        // left
    }
};
