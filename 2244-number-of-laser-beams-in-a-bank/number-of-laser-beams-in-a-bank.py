class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        import math
        total_beams= 0 
        row_lst = []
        for i in bank:
            row_lst.append(i.count('1'))
        
        r1 = 0
        for i in row_lst:
            total_beams += r1 * i
            if i > 0:
                r1 = i
        return total_beams
        
                

