class Solution:
    def largestNumber(self, arr: List[int]) -> str:
        l = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                a = str(arr[i])
                b = str(arr[j])
                if a+b < b+a:
                    arr[i] = int(b)
                    arr[j] = int(a)
        arr = list(map(str,arr))
        return ''.join(arr) if arr.count('0') != len(arr) else '0'
