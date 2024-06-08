class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_dict = {0: -1}
        cumulative_sum = 0
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            if k != 0:
                cumulative_sum %= k
            
            if cumulative_sum in remainder_dict:
                
                if i - remainder_dict[cumulative_sum] > 1:
                    return True
            else:
                
                remainder_dict[cumulative_sum] = i
        
        return False