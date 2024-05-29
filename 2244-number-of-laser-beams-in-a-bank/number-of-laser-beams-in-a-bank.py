class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        import math
        total_beams= 0 
        r1 = 0
        
        for i in bank:
            d=i.count('1')
            if d > 0:
                total_beams += r1 * d
                r1 = d
        return total_beams
        
                

