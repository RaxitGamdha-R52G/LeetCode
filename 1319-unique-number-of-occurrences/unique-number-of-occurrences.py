class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        arr = Counter(arr)
        arr=list(arr.values())
        for i in arr:
            if arr.count(i) > 1:
                return False
        return True