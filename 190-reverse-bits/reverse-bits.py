class Solution:
    def reverseBits(self, n: int) -> int:
        f = bin(n)[2:]
        s = '0'*(32-len(f))+f
        return int('0b'+s[::-1],2)

