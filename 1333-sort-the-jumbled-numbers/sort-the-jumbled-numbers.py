class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        l_map = []
        for num in nums:
            d = ''.join([str(mapping[int(i)]) for i in str(num)])
            l_map.append([int(d),num])
        l_map.sort(key=lambda x:x[0])
        return [i[1] for i in l_map]

        