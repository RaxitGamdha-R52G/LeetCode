class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        result = []
        length = len(words)

        def backtrack(a_score, letters, curr):
            if curr == length:
                result.append(a_score)
                return
            
            flag = True
            temp = 0
            v = letters.copy()
            for ch in words[curr]:
                if v[ch] > 0:
                    temp += score[ord(ch) - 97]
                    v[ch] -= 1
                else:
                    flag = False
                    break
            
            if flag:
                backtrack(a_score+temp,v,curr+1)          
            backtrack(a_score,letters,curr+1)
        
        backtrack(0, Counter(letters), 0)
        return max(result)