class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_arr = [0]
        for i in arr:
            prefix_arr.append(prefix_arr[-1]^i)

        result = [prefix_arr[r+1] ^ prefix_arr[l] for l,r in queries]

        return result