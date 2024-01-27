class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        d=x[::-1]

        return True if d==x else False
        