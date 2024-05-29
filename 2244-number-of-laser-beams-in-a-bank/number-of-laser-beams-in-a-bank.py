class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        import math
        total_beams= 0 
        row_lst = []
        for i in bank:
            row_lst.append(i.count('1'))
        
        r1 = 0
        r2 = 0
        for i in row_lst:
            if i > 0:
                if r1 == 0:
                    r1 = i
                    continue
                if r2 == 0:
                    r2 = i
                total_beams += r1 * r2
                r1 = r2
                r2 = 0
        return total_beams
        
                

