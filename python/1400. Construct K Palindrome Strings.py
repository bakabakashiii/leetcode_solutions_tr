class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        freq = Counter(s)
        odd = 0
        for i in freq.values():
            odd += i % 2

        return odd <= k
        
