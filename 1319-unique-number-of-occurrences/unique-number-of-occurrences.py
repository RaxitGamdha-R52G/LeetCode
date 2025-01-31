class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        arr = Counter(arr)
        arr=list(arr.values())
        arrSet = list(set(arr))
        return sorted(arrSet) == sorted(arr)