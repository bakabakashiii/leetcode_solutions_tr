class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts = {}

        for word in words2:
            letters = Counter(word)
            for a, b in letters.items():
                if a in counts:
                    counts[a] = max(counts[a], b)
                else:
                    counts[a] = b

        ans = []
        for word in words1:
            letters = Counter(word)
            isValid = True

            for a in counts:
                if letters.get(a, 0) < counts[a]:
                    isValid = False
                    break
                    
            if isValid:
                ans.append(word)
                    
        return ans
