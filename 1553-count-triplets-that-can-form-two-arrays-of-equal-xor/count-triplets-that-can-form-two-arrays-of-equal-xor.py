class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        
        for i in range(n):
            xor_sum = 0
            for k in range(i, n):
                xor_sum ^= arr[k]
                if xor_sum == 0 and k > i:
                    count += k - i
        
        return count
            


        