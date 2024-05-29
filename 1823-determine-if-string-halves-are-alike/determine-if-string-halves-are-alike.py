class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        from collections import Counter
        s1 = Counter(s1.lower())
        s2 = Counter(s2.lower())

        def count(s):
            c=0
            for i in s:
                if i in 'aeiou':
                    c += s[i]
            
            return c
        return count(s1) == count(s2)

        