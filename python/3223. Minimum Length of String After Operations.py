class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        ans = len(s)

        for i in counter.values():
            while i >= 3:
                i -= 2
                ans -= 2

        return ans
