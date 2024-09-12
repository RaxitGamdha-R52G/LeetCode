class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        p1 = None
        N = len(nums)
        for i in range(N-1,0,-1):
            if nums[i] > nums[i - 1]:
                p1 = i - 1
                break
        if p1 is None:
            nums.sort()
            return
        p2 = N-1
        for j in range(N-1,p1,-1):
            if nums[j] > nums[p1]:
                p2 = j
                break
        nums[p2],nums[p1] = nums[p1], nums[p2]
        
        for i in range(p1+1,N-1):
            for j in range(i+1,N):
                if nums[i] > nums[j]:
                    nums[j],nums[i] = nums[i], nums[j]
