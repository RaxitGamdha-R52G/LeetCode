class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        count=0
        for i in range(len(nums)-1) :
            if nums[i]!=nums[i+1]or count==2:
                count=0
                nums[k]=nums[i]
                k+=1
            elif nums[i]==nums[i+1] and count<1:
                count+=1
                nums[k]=nums[i]
                k+=1
        nums[k]=nums[len(nums)-1]   
        return k+1