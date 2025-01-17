class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = dict()
        for index, letter in enumerate(s):
            if letter in mapping:
                if mapping[letter] != t[index]:
                    return False
            else:
                if t[index] in mapping.values():
                    return False
                mapping[letter] = t[index]
        return True