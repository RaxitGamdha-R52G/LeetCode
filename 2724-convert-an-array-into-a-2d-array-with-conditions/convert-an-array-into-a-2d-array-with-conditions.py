class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result=[]
        a=list(set(nums))
        result.append(a)
        for i in a:
            nums.remove(i)
        if nums != []:
            result.extend(self.findMatrix(nums))
        
        return result