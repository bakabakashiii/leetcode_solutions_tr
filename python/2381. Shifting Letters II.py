class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftAmount = [0] * (len(s) + 1) 

        for l, r, d in shifts: 
            if d == 0: 
                shiftAmount[l] -= 1 
                shiftAmount[r+1] += 1
            else: 
                shiftAmount[l] += 1
                shiftAmount[r+1] -= 1 

        shiftss = 0
        s = list(s)
        for i in range(len(s)): 
            shiftss += shiftAmount[i]

            cur = (((ord(s[i]) + shiftss) - 97) % 26) + 97 
            s[i] =  chr(cur)
        
        return ''.join(s)
