class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        d= min(len(word1),len(word2))
        result = []
        i = 0

        while i < d:
            result.append(word1[i])
            result.append(word2[i])
            i+=1
        result+= word1[i:]
        result+= word2[i:]

        return ''.join(result)
        
        