class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = defaultdict(str)
        length = len(s)
        for i in range(length):
            if mapping[s[i]] and mapping[s[i]] != t[i]:
                return False
            else:
                d = set(filter(lambda key:mapping[key]==t[i], mapping))
                if len(d) > 0 and s[i] not in d:
                    return False
            mapping[s[i]] = t[i]
        
        return True
        