class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        indexes = {}
        rFreq = [0] * rows
        cFreq = [0] * cols

        for r in range(rows):
            for c in range(cols):
                indexes[mat[r][c]] = (r, c)
                
        for i in range(len(arr)):
            r, c = indexes[arr[i]]
            rFreq[r] += 1
            cFreq[c] += 1
            if rFreq[r] == cols or cFreq[c] == rows: return i
