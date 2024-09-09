class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        A, B = len(word1), len(word2)
        i = 0
        result = []
        while i < A or i < B:
            if i < A:
                result.append(word1[i])
            if i < B:
                result.append(word2[i])
            i += 1

        return ''.join(result)
        
        