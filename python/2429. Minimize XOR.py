class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countBits(n):
            res = 0
            while n>0:
                res += 1 & n
                n = n >> 1
            return res

        bits1, bits2 = countBits(num1), countBits(num2)
        x = num1
        i = 0

        while bits1 > bits2:
            if  x & (1 << i):
                bits1 -= 1
                x = x ^ (1 << i)
            i += 1

        while bits1 < bits2:
            if  x & (1 << i) == 0:
                bits1 += 1
                x = x | (1 << i)
            i += 1

        return x
