class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        rowList = [0] * rows
        colList = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowList[r] += 1
                    colList[c] += 1
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (rowList[r] + colList[c]) > 2:
                    ans+=1
        
        return ans
