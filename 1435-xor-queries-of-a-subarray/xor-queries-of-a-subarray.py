class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_arr = [0]
        result = []
        for i in arr:
            prefix_arr.append(prefix_arr[-1]^i)
        for l,r in queries:
            result.append(prefix_arr[r+1] ^ prefix_arr[l])

        return result