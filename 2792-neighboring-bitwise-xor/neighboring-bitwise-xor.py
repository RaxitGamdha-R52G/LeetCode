class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # return sum(derived) % 2 == 0
        a = 0
        for i in derived:
            if i:
                a = ~ a
        
        return a == 0
        