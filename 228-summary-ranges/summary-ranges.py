class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        num = float('-inf')
        for i in nums:
            if i<= num:
                continue
            num = i
            while num +1 in nums:
                num += 1
            if num == i:
                result.append(str(num))
            else:
                result.append(str(i)+'->'+str(num))
        return result
            
        