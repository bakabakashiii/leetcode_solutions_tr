class Solution:
    def highestPeak(self, is_water):
        rows, cols = len(is_water), len(is_water[0])
        q = deque()
        ans = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if is_water[r][c] == 1:
                    q.append((r, c))
                    ans[r][c] = 0
        
        while q:
            r, c = q.popleft()
            h = ans[r][c]

            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or 
                nr == rows or nc == cols or
                ans[nr][nc] != -1):
                    continue
                q.append((nr, nc))
                ans[nr][nc] = h + 1

        return ans
