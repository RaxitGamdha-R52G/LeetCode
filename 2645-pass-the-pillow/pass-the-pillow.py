class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = 1
        v = 1
        for i in range(time):
            if v == n:
                d = -1
            elif v == 1:
                d = 1
            v += d
        return v
