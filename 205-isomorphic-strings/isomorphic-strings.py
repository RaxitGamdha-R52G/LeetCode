class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = defaultdict(str)
        length = len(s)
        for i in range(length):
            if mapping[s[i]] and mapping[s[i]] != t[i]:
                return False
            else:
                d = set(filter(lambda key:mapping[key]==t[i], mapping))
                for el in d:
                    if el != s[i]:
                        return False
            mapping[s[i]] = t[i]
        
        return True
        