class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        d= min(len(word1),len(word2))
        i = 0

        while i < d:
            result+= word1[i]+word2[i]
            i+=1
        result+= word1[i:]
        result+= word2[i:]

        return result
        
        