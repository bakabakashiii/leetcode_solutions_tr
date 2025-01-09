class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set()
        ans = 0

        for i in s:
            letters.add(i)

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            temp = set()

            for k in range(i+1,j):
                temp.add(s[k])

            ans+=len(temp)

        return ans
