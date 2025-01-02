2559. Count Vowel Strings in Ranges

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        dp = [0] * (n + 1)
        vowel = 'aeiou'
        ans = []
        for i in range(n):
            dp[i + 1] = dp[i] + (1 if words[i][0] in vowel and words[i][-1] in vowel else 0)
        for l, r in queries:
            ans.append(dp[r + 1] - dp[l])
        return ans
