class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        l = len(nums)
        l_arr = self.sortArray(nums[:l//2])
        r_arr = self.sortArray(nums[l//2:])

        return self.join(l_arr,r_arr)

    def join(self,l_arr,r_arr):
        i = 0
        j = 0
        result = []
        while(i< len(l_arr) and j <len(r_arr)):
            if l_arr[i] < r_arr[j]:
                result.append(l_arr[i])
                i += 1
            else:
                result.append(r_arr[j])
                j += 1
        
        while i< len(l_arr):
            result.append(l_arr[i])
            i += 1
        while j< len(r_arr):
            result.append(r_arr[j])
            j += 1
        
        return result