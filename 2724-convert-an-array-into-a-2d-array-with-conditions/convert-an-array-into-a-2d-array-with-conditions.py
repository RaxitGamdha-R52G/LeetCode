class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result=[]
        while nums != []:
            a=list(set(nums))
            result.append(a)
            for i in a:
                nums.remove(i)
        
        return result