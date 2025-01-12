class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        curLeft = 0
        curRight = 0

        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                curLeft += 1
            else:
                if curLeft == 0:
                    return False
                curLeft -= 1
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                curRight += 1
            else:
                if curRight == 0:
                    return False
                curRight -= 1

        return True
