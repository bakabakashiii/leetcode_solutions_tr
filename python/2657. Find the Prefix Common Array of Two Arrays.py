class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        seen = [0] * (len(A) + 1)
        common = 0
        
        for i in range(len(A)):
            if seen[A[i]] == 0:
                seen[A[i]] = 1
            elif seen[A[i]] == 1:
                common += 1
            if seen[B[i]] == 0:
                seen[B[i]] = 1
            elif seen[B[i]] == 1:
                common += 1
            ans.append(common)
        return ans
