class Solution:
    def isPalindrome(self, s: str) -> bool:
        d="".join(i for i in s.lower() if (96<ord(i) and ord(i)<=122) or (47<ord(i) and ord(i)<=57))
        return d[::]==d[::-1]