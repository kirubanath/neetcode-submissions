"""
Reverse means 
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):

            mask = 1 << i
            bit  = n & mask

            if bit:
                res = res | (1 << (31-i))

        
        return res