class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l=-1
        u=2
        r=1
        d=-2
        p=[0,0]
        for i in moves:
            if i=="L":
                p[0]+=l
            elif i=="R":
                p[0]+=r
            elif i=="U":
                p[1]+=u
            elif i=="D":
                p[1]+=d
        
        if p==[0,0]:
            return True
        else:
            return False