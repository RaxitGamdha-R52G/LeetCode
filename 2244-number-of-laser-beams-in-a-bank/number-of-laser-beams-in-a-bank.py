class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        import math
        total_beams= 0 
        row_lst = []
        for i in bank:
            row_lst.append(i.count('1'))
        
        r1 = 0
        for i in row_lst:
            if i > 0:
                total_beams += r1 * i
                r1 = i
        return total_beams
        
                

