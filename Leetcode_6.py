class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only one row, or fewer characters than rows
        if numRows == 1 or numRows >= len(s):
            return s

        # Prepare buckets for each row
        rows = [""] * numRows
        row = 0
        down = False  # direction flag

        for ch in s:
            rows[row] += ch
            
            # flip direction at top/bottom
            if row == 0 or row == numRows - 1:
                down = not down
            
            # move pointer
            row += 1 if down else -1

        # join rows together
        return "".join(rows)
