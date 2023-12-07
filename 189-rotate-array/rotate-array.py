class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        while i<k:
            d=nums.pop()
            nums.insert(0,d)
            i+=1
        
        