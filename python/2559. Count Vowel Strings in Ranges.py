class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        letters = ('a', 'e', 'i', 'o', 'u')
        def isValid(word):
            if word[0] in letters and word[len(word)-1] in letters:
                return True
            return False
        
        numOfValid = [0]
        amount = 0
        for i in range(len(words)):
            if isValid(words[i]):
                amount += 1
            numOfValid.append(amount)

        ans = []
        for i in queries:
            ans.append(numOfValid[i[1] + 1] - numOfValid[i[0]])

        return ans
