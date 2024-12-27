class Solution:
    def findComplement(self, num: int) -> int:
        num_b = bin(num)[2:]
        num_l = len(num_b)

        max_n = '0b'+'1'*num_l

        result = num^int(max_n,2)
        return result
        