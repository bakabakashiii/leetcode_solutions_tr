class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        i, j = 0, 0
        for k in range(len(boxes)):
            ans[k] = i + j
            j += i
            i += int(boxes[k])
        
        i, j = 0, 0
        for k in reversed(range(len(boxes))):
            ans[k] += i + j
            j += i
            i += int(boxes[k])

        return ans
