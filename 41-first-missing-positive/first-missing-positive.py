class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left_min = 1
        hmap = defaultdict(int)
        for i in nums:
            if i > 0:
                hmap[i] = 1
                while hmap[left_min] > 0:
                    del hmap[left_min]
                    left_min += 1
                
        
        return left_min
        