class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # from itertools import permutations
        # per_arr = list(permutations(nums))
        # result = list(map(list,per_arr))
        # return result
        result = []
        self.permutations(nums,[],result)
        return result

    def permutations(self,arr, temp, result_arr):
        if not arr:
            result_arr.append(temp)

        for i in range(len(arr)):
            self.permutations(arr[:i]+arr[i+1:],temp + [arr[i]],result_arr)
